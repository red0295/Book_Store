from rest_framework import serializers
from .models import Product,Cart,Wishlist,Order,Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields='__all__' 

class ProductSerializer(serializers.ModelSerializer):
    genre=serializers.StringRelatedField()
    class Meta:
        model=Product
        fields='__all__'
class CartSerializer(serializers.ModelSerializer):
    product=ProductSerializer(many=True)
    
    class Meta:
        model=Cart
        fields=['product']
class WishlistSerializer(serializers.ModelSerializer):
    product=ProductSerializer(many=True)
    
    class Meta:
        model=Wishlist
        fields=['product']
class OrderSerializer(serializers.ModelSerializer):
    product=ProductSerializer(many=True)
    
    class Meta:
        model=Order
        fields=['product','total_price']
