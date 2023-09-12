from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('change_pswd',views.change_pswd,name='change_pswd'),
    path('forgot_pswd',views.forgot_pswd,name='forgot_pswd'),
    path('verify_otp',views.verify_otp,name='verify_otp'),
    path('create_pswd',views.create_pswd,name='create_pswd'),
    path('seller_index',views.seller_index,name='seller_index'),
    path('seller_change_pswd',views.seller_change_pswd,name='seller_change_pswd'),
    path('seller_add_product',views.seller_add_product,name='seller_add_product'),
    path('myproduct',views.myproduct,name='myproduct'),
    path('seller_product_edit/<int:pk>/',views.seller_product_edit,name='seller_product_edit'),
    path('seller_product_delete/<int:pk>/',views.seller_product_delete,name='seller_product_delete'),
    path('product',views.product,name='product'),
    path('product_details/<int:pk>/',views.product_details,name='product_details'),
    path('add_to_wishlist/<int:pk>/',views.add_to_wishlist,name='add_to_wishlist'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('remove_from_wishlist/<int:pk>/',views.remove_from_wishlist,name='remove_from_wishlist'),
    path('add_to_cart/<int:pk>/',views.add_to_cart,name='add_to_cart'),
    path('cart',views.cart,name='cart'),
    path('remove_from_cart/<int:pk>/',views.remove_from_cart,name='remove_from_cart'),
    path('change_qty/<int:pk>/',views.change_qty,name='change_qty'),
    path('search',views.search,name='search'),
    path('success',views.success,name='success'),
    path('ajax/form_validation/',views.form_validation,name='form_validation'),
    path('tarnsaction',views.tarnsaction,name='tarnsaction'),
]
