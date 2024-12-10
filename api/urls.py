from django.urls import path
from .views import hello_world, another_endpoint  # Import your view function

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('another/', another_endpoint, name='another_endpoint'),
]