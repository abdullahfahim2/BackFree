from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('process/', views.process_image, name='process_image'),
    path('result/<int:pk>/', views.result, name='result'),
]