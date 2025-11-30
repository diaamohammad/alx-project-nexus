from rest_framework import viewsets, permissions, generics, filters
from rest_framework.response import Response
from .models import Product, CustomUser, Category
from .serializers import (
    UserRegisterSerializer,
    UserSerializer,
    CategorySerializer,
    ProductReadSerializer,
    ProductWriteSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend 

# 1. Register View
class UserRegister(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer

# 2. User View (Admin Only)
class UserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAdminUser] 

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return UserSerializer
        return UserRegisterSerializer

# 3. Category View
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('price')

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    
    filterset_fields = ['category', 'price']

    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
    
    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return ProductReadSerializer
        return ProductWriteSerializer
    
