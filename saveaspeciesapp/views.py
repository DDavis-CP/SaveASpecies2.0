from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

 #Class based view that combines the Landing template and a context dictionary that returns an HTTP response with the rendered arguments
class Landingview(View):
    def get(self, request):
        return render( request=request , template_name ="landing_page.html", context = {})
 #Class based view that combines the Home template and a context dictionary that returns an HTTP response with the rendered arguments
class Homeview(View):
    def get(self, request):
        return render( request=request , template_name ="home.html", context = {})
 #Class based view that combines the animal_type template and a context dictionary that returns an HTTP response with the rendered arguments
class Animaltypeview(View):
    def get(self, request):
        return render( request=request , template_name ="animal_type.html", context = {})
 #Class based view that combines the animal_species template and a context dictionary that returns an HTTP response with the rendered arguments
class Animalspeciesview(View):
    def get(self, request):
        return render( request=request , template_name ="animal_species.html", context = {})
 #Class based view that combines the source_page template and a context dictionary that returns an HTTP response with the rendered arguments
class Sourcesview(View):
    def get(self, request):
        return render( request=request , template_name ="source_page.html", context = {})
 #Class based view that combines the source_page template and a context dictionary that returns an HTTP response with the rendered arguments
class Searchview(View):
    def get(self, request):
        return render( request=request , template_name ="search_page.html", context = {})