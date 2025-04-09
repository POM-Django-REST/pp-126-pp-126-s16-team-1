from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import OrderViewSet, UserOrderDetail

router = DefaultRouter()
router.register(r'', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:user_id>/order/<int:order_id>/', UserOrderDetail.as_view(), name='user_order_detail'),
]
