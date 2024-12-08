from django.contrib import admin
from django.urls import path, include  # Include is required for app-level URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel routes
    path('api/', include('api.urls')),  # Includes app-specific URLs
]