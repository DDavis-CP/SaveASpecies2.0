from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views import *
from saveaspeciesapp.views import *


urlpatterns = [
    #creates a path to reference the Landingview in the view.py file that points to the landing_page template
    path('landing/', Landingview.as_view(), name = 'landing')
]