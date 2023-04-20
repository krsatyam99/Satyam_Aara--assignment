from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

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
