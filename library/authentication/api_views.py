from rest_framework import generics
from authentication.models import CustomUser
from .serializers import UserSerializer
from order.models import Order
from order.serializers import OrderSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserOrderDetailAPIView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        order_id = self.kwargs.get('order_id')
        return Order.objects.get(pk=order_id, user_id=user_id)