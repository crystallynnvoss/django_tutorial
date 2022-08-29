"""storefront URL Configuration

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
    2. Add a URL to urlpatterns:  path('a_route/', include('a_route.urls')) #call path, 
    give it a route, then include function to reference the url config module in this app.
"""
from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [ #array of urlpattern objects
    path("admin/", admin.site.urls),
    path("newplay/", include("newplay.urls")), #so any reference to newplay in the urls followed by / should be routed to newplay app
    path('__debug__/', include('debug_toolbar.urls')),
]

