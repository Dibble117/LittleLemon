from django.contrib import admin 
from django.urls import path 
from .views import sayHello
from . import views
from rest_framework.authtoken.views import obtain_auth_token
  
urlpatterns = [ 
    path('', sayHello, name='sayHello'),
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', views.BookingViewSet.as_view({'get': 'list'})),
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]