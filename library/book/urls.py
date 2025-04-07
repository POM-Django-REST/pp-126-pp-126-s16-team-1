from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookCreateView, BookUpdateView

router = DefaultRouter()
router.register(r'book', BookViewSet, basename='book')

urlpatterns = [
    # DRF API
    path('', include(router.urls)),

    # Старі CBV
    path('books/add/', BookCreateView.as_view(), name='book_add'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
]
