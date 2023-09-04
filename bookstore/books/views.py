from rest_framework import generics
from .models import Genre,Product,Cart,Wishlist,Order
from .serializers import ProductSerializer, CartSerializer, WishlistSerializer, OrderSerializer,GenreSerializer

# Create your views here.
class GenreCreateView(generics.CreateAPIView):
    queryset=Genre.objects.all()
    serializer_class=GenreSerializer
class ProductListView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
class ProductCreateView(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
class ProductUpdateView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
class ProductDeleleView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
class CartView(generics.RetrieveUpdateAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer

class WishlistView(generics.RetrieveUpdateAPIView):
    queryset=Wishlist.objects.all()
    serializer_class=WishlistSerializer
class orderView(generics.RetrieveUpdateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

