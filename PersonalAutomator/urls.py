from django.contrib import admin
from django.urls import path, include  # Include is required for app-level URLs
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to the Django API</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel routes
    path('api/', include('api.urls')),  # Includes app-specific URLs
    path('', home_view, name='home'),
]