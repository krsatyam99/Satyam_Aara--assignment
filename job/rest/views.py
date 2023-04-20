from django.shortcuts import render

# Create your views here.
from rest_framework import status
from .models import Shop as ShopModel

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from django.contrib.auth import authenticate


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        # print("user:")
        # print(username)
        # print(password)
        user = authenticate(username=username, password=password)
        # print("user:")
        # print(user)
        if user:
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({
                'error': 'Invalid credentials',
            }, status=status.HTTP_401_UNAUTHORIZED)
        


class S_list(APIView):
    
    def get(self, request):
        longitude = request.query_params.get('longitude')
        latitude = request.query_params.get('latitude')

        if not longitude or not latitude:
            return Response({'error': 'Longitude and latitude parameters are required.'}, status=400)

        try:
            longitude = float(longitude)
            latitude = float(latitude)
        except ValueError:
            return Response({'error': 'Longitude and latitude parameters must be numbers.'}, status=400)

        # Query the Shop model for nearby shops
       
        nearby_shops = ShopModel.objects.filter(
            longitude__range=(float(longitude) - 0.10, float(longitude) + 0.10),
        latitude__range=(float(latitude) - 0.10, float(latitude) + 0.10)
)

        serializer = ShopSerializer(nearby_shops, many=True)

        return Response(serializer.data)

class Shop(APIView):
  def post(self, request, format=None):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":'Successfully registered' } ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class shopId(APIView):
    def get(self, request, format=None):
        mobile = request.query_params.get('mobile', None)
        name = request.query_params.get('name', None)
        if mobile and name:
            try:
                shop = ShopModel.objects.get(mobile=mobile, name=name)
                data = {
                    'id': shop.shop_id,
                    'name': shop.name
                }
                return Response(data)
            except ShopModel.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class ShopReview(APIView):
    def post(self, request):
        # Deserialize the request data
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            # Get the shop ID from the request data
            shop_id = serializer.validated_data['shop'].shop_id
            # Check if the shop exists
            try:
                shop = ShopModel.objects.get(shop_id=shop_id)
            except ShopModel.DoesNotExist:
                return Response({'error': 'Shop not found.'}, status=status.HTTP_404_NOT_FOUND)

            # Create the review object
            review = serializer.save()

            # Add the review to the shop's reviews
            shop.reviews.add(review)

            # Serialize the review data
            review_serializer = ReviewSerializer(review)

            # Return the serialized review data
            return Response(review_serializer.data, status=status.HTTP_201_CREATED)

        # If the data is not valid, return an error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ShopInfo(APIView):
    def get(self, request):
        # Get the request parameters
        shop_id = request.query_params.get('shop_id', None)
        name = request.query_params.get('name', None)

        # If both shop_id and name are provided, search for the shop by shop_id
        if shop_id is not None and name is not None:
            try:
                shop = ShopModel.objects.get(shop_id=shop_id, name=name)
            except ShopModel.DoesNotExist:
                return Response({'error': 'Shop not found.'}, status=status.HTTP_404_NOT_FOUND)
        # If only name is provided, search for the shop by name
        elif name is not None:
            try:
                shop = ShopModel.objects.get(name=name)
            except ShopModel.DoesNotExist:
                return Response({'error': 'Shop not found.'}, status=status.HTTP_404_NOT_FOUND)
        # If only shop_id is provided, search for the shop by shop_id
        elif shop_id is not None:
            try:
                shop = ShopModel.objects.get(shop_id=shop_id)
            except ShopModel.DoesNotExist:
                return Response({'error': 'Shop not found.'}, status=status.HTTP_404_NOT_FOUND)
        # If no parameters are provided, return an error response
        else:
            return Response({'error': 'Please provide either shop_id or name as a request parameter.'}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize the shop data
        shop_serializer = ShopSerializer(shop)

        # Get the reviews for the shop
        reviews = Review.objects.filter(shop=shop)

        # Serialize the review data
        review_serializer = ReviewSerializer(reviews, many=True)

        # Return a dictionary with the shop and review data
        return Response({'shop': shop_serializer.data, 'reviews': review_serializer.data}, status=status.HTTP_200_OK)
