from django.urls import path
from . import views as art_site_views

urlpatterns = [
    path('',art_site_views.home,name="home"),
]