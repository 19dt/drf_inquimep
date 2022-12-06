"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from mainapp import urls
from rest_framework.authtoken import views
from mainapp.views import Login, Logout
from mainapp.routers import router

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('mainapp/', include(('mainapp.urls', 'mainapp' ))),
    path('entry/', include('mainapp.urls')),
    path('analysis/', include('analysis.urls')),
    path('api_generate_token/', views.obtain_auth_token),
    path('login/', Login.as_view(), name = 'login'),
    path('logout/', Logout.as_view(), name = 'logout'),
]

urlpatterns += router.urls
