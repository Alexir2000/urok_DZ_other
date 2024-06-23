from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.func_new),
    path('data/', views.func_data, name='func_data'),
    path('test/', views.func_test, name='func_test')
]