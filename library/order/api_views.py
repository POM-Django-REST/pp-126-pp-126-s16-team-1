from rest_framework import viewsets, generics
from rest_framework.exceptions import PermissionDenied
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            raise PermissionDenied("Authentication credentials were not provided.")


class UserOrderDetail(generics.RetrieveAPIView):
    serializer_class = OrderSerializer

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        order_id = self.kwargs.get('order_id')
        return Order.objects.get(pk=order_id, user_id=user_id)
