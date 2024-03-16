from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class Landingview(View):
    def get(self, request):
        return render( request=request , template_name = "landing_page.html", context = {})