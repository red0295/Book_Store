from rest_framework import generics
from .models import Genre,Product,Cart,Wishlist,Order
from .serializers import ProductSerializer, CartSerializer, WishlistSerializer, OrderSerializer,GenreSerializer
from rest_framework.response import Response

# Create your views here.
class GenreCreateView(generics.CreateAPIView):
    queryset=Genre.objects.all()
    serializer_class=GenreSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class ProductListView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def get(self,request,*args,**kwargs):
        products=self.get_queryset()
        serializer=self.get_serializer(products,many=True)
        return Response(serializer.data)
class ProductCreateView(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class ProductUpdateView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class ProductDeleleView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)
    
class CartView(generics.RetrieveUpdateAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
    
    def get(self, request, *args, **kwargs):
        cart = self.get_object()
        serializer = self.get_serializer(cart)
        return Response(serializer.data)

class WishlistView(generics.RetrieveUpdateAPIView):
    queryset=Wishlist.objects.all()
    serializer_class=WishlistSerializer
    
    def get(self, request, *args, **kwargs):
        wishlist = self.get_object()
        serializer = self.get_serializer(wishlist)
        return Response(serializer.data)
    
class orderView(generics.RetrieveUpdateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    
    def get(self, request, *args, **kwargs):
        order = self.get_object()
        serializer = self.get_serializer(order)
        return Response(serializer.data)

