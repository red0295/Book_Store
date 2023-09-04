
from django.urls import path
from .views import ProductListView,ProductCreateView,ProductUpdateView,ProductDeleleView,CartView,WishlistView,orderView,GenreCreateView

urlpatterns = [
    path('api/genre/create/',GenreCreateView.as_view(),name='genre-create'),
    path('api/products/',ProductListView.as_view(),name='product-list'),
    path('api/products/create/',ProductCreateView.as_view(),name='product-create'),
    path('api/products/update/<int:pk>/',ProductUpdateView.as_view(),name='product-update'),
    path('api/products/delete/<int:pk>/',ProductDeleleView.as_view(),name='product-delete'),
    path('api/cart/',CartView.as_view(),name='cart'),
    path('api/wishlist',WishlistView.as_view(),name='wishlist'),
    path('api/orders/create/',orderView.as_view(),name='order-create'),
]