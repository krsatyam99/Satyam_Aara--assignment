# Shop Apis
Django Rest Framework Project
Introduction:

This is a Django Rest Framework project that uses Simple JWT for authentication and Django's built-in User model for user management.


Register and login Api flow


![WhatsApp Image 2023-04-20 at 19 26 38 (1)](https://user-images.githubusercontent.com/103446420/233403316-a8061bc3-bab2-4a87-86cd-84bdbc7ed083.jpeg)


Along with that , I have developed Apis which create and retrive  Shop data according to user's location or entering shop name.

The following API flow diagrams illustrate the steps involved in making requests to the various endpoints:
Shop Apis flow
![WhatsApp Image 2023-04-20 at 19 26 38](https://user-images.githubusercontent.com/103446420/233403388-ff07bb7a-0770-4586-bfe4-f6a6fc2bdf40.jpeg)

Installation
To install the required packages, run the following command:

Copy code
pip install -r requirements.txt



API Endpoints
The following API endpoints are available:

urlpatterns = [

    path('api/register/', RegistrationAPIView.as_view(), name='register'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('login/', Login.as_view()),
    
    path('shops/', S_list.as_view(), name='shop-list'),
    
    path('createshops/', Shop.as_view(), name='create_shop'),
    
    path('shop_id/', shopId.as_view()),
    
    path('reviews/', ShopReview.as_view(), name='review-create'),
    
    path('info/', ShopInfo.as_view()),
]


Postman Collection
A Postman collection is available for testing the API endpoints. You can import the collection by clicking the following link:

Postman Collection Link
https://api.postman.com/collections/24162967-cfd44ad3-9d4d-40be-83eb-fd4bc6178d99?access_key=####


Video Link
A video demonstration of the project is available at the following link:

Video Link:
https://youtu.be/9ekIRz5xbUQ
