from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views import *
from saveaspeciesapp.views import *


urlpatterns = [
    #creates a path to reference the Landingview in the view.py file that points to the landing_page template
    path('', Landingview.as_view(), name='landing'),
    path('home/', Homeview.as_view(), name='home'),
    path('animal_type/', Animaltypeview.as_view(), name='animal_type'),
    path('animal_type/animal_species/', Animalspeciesview.as_view(), name='animal_type'),
    path('animal_type/animal_species/source_page/', Sourcesview.as_view(), name='source_page'),
    path('search/', Searchview.as_view(), name='source_page'),
]