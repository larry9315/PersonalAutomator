from django.urls import path
from .views import hello_world  # Import your view function

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),  # Matches /api/hello/
]