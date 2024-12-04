"""
URL configuration for mypersonalsite project.

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
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static


# URL configuration for the project
urlpatterns = [
    #path('admin/', admin.site.urls),
    #include the portfolio app URLs
    #path('', include('portfolio.urls')),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #to add media content 

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),  # Admin URLs
    path('', include('portfolio.urls')),  # Include your app's URLs
) 