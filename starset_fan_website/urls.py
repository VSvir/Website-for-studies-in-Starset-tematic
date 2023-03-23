"""djangoStarsetWebsiteProject URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('band', views.band, name='band'),
    path('society', views.society, name='society'),
    path('feedback', views.feedback, name='feedback'),
    path('transmissions_cover', views.transmissions, name='transmissions'),
    path('divisions_cover', views.divisions, name='divisions'),
    path('horizons_cover', views.horizons, name='horizons'),
    path('vessels_cover', views.vessels, name='vessels'),
    path('vessels_cover_2', views.vessels_2, name='vessels_2'),
    path('form_response', views.form_response, name='form_response'),
]
