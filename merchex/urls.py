"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from listing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', view=views.bands, name="bands"),
    path('bands/<int:band_id>/', view=views.band_details, name="band_details"),
    path('bands/add/', view=views.band_create, name="band_create"),
    path('bands/<int:band_id>/update/',
         view=views.band_update, name="band_update"),
    path('bands/<int:band_id>/delete/',
         view=views.band_delete, name="band_delete"),
    path('listings/', view=views.listings, name="listings"),
    path('listings/<int:id>/', view=views.listing_details, name="listing_details"),
    path('listings/add/', view=views.listing_create, name="listing_create"),
    path('listings/<int:id>/update/',
         view=views.listing_update, name="listing_update"),
    path('listings/<int:id>/delete/',
         view=views.listing_delete, name="listing_delete"),
    path('about/', view=views.about),
]
