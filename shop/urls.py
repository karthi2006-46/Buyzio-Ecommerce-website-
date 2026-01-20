from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path("addtocart/", views.add_to_cart, name="add_to_cart"),
    path("fav/", views.add_to_fav, name="add_to_fav"),
    path("cart/", views.cart_page, name="cart"),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('remove_cart/<str:cid>', views.remove_cart , name="remove_cart"),
  
    path('collections/', views.collections, name="collections"),
    path('collections/<str:name>/', views.collectionsview, name="collectionsview"),

    # 🔥 use product id instead of pname
    path('collections/<str:cname>/<int:pid>/', views.product_details, name="product_details"),

  

]
