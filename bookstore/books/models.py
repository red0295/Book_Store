from django.db import models
from accounts.models import User

# Create your models here.
class Genre(models.Model):
    name=models.CharField(max_length=100, unique=True)
    image=models.ImageField(upload_to='products/')
    
    class Meta:
        ordering=('-name',)
        verbose_name_plural='genres'
    def __str__(self):
        return self.name
class Product(models.Model):
    genre=models.ForeignKey(Genre, related_name='products', on_delete=models.CASCADE)
    productName=models.CharField(max_length=100)
    productDescription=models.TextField()
    productPrice=models.DecimalField(max_digits=10, decimal_places=2)
    productSalePrice=models.DecimalField(max_digits=10, decimal_places=2)
    productImage=models.ImageField(upload_to='products/')
    productType=models.CharField(max_length=100)
    productStatus=models.CharField(max_length=100)
    productSKU=models.CharField(max_length=100)
    
    class Meta:
        ordering=('productName',)
    def __str__(self):
        return self.productName
class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    product=models.ManyToManyField(Product)
    quantity=models.PositiveBigIntegerField(default=1)
class Wishlist(models.Model):
   user=models.OneToOneField(User,on_delete=models.CASCADE)
   product=models.ManyToManyField(Product)
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ManyToManyField(Product)
    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)