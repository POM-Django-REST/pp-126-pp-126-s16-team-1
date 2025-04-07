from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, AuthorCreateView, AuthorUpdateView

router = DefaultRouter()
router.register(r'author', AuthorViewSet, basename='author')

urlpatterns = [
    # DRF API
    path('', include(router.urls)),

    # Старі CBV
    path('authors/add/', AuthorCreateView.as_view(), name='author_add'),
    path('authors/<int:pk>/edit/', AuthorUpdateView.as_view(), name='author_edit'),
]
