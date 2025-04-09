from django.urls import path
from .api_views import UserCreateAPIView, UserDetailAPIView, UserOrderDetailAPIView

urlpatterns = [
    path('', UserCreateAPIView.as_view(), name='api_user_create'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='api_user_detail'),
    path('<int:user_id>/order/<int:order_id>/', UserOrderDetailAPIView.as_view(), name='api_user_order_detail'),
]
