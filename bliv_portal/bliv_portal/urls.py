"""
URL configuration for bliv_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from bliv_app import views as bliv_app_views
from perfil import views as perfil_views
from rest_framework import routers


route = routers.DefaultRouter()

urlpatterns = [
    path('', include('bliv_app.urls')),
    path('admin/', admin.site.urls),
    path('apibooks/', bliv_app_views.api_livros),
    path('signup/', include('bliv_app.urls')),  # Para signup
    path('login/', include('bliv_app.urls')),   # Para login
    path('api', include(route.urls))
 ] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

