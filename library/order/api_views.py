from rest_framework import viewsets, generics
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class UserOrderDetail(generics.RetrieveAPIView):
    serializer_class = OrderSerializer

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        order_id = self.kwargs.get('order_id')
        return Order.objects.get(pk=order_id, user_id=user_id)
