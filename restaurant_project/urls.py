"""
URL configuration for restaurant_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from django.conf.urls import handler404, handler500
from django.shortcuts import render
from django.views.generic import TemplateView

# view for the error page defined
def custom_error_page(request, exception=None):
    return render(request, 'error.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookings.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = custom_error_page  # Handles 404 errors
handler500 = custom_error_page  # Handles 500 errors

