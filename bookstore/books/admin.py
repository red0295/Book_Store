from django.contrib import admin
from .models import Genre,Product
# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display=('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('productName','genre','productDescription','productPrice','productSalePrice','productType','productStatus','productSKU')
    list_filter=('genre','productStatus')
    list_editable=('productPrice','productSalePrice','productStatus')