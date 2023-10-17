from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('register/', views.userRegister, name='register'),

    path('add/<str:pk>/', views.addToCart, name='add'),
    path('remove/<str:pk>/', views.removeItem, name='remove-item'),
    path('mycart/<str:pk>/', views.myCart, name='mycart'),
    path('upload/', views.uploadProduct, name='upload'),
]
