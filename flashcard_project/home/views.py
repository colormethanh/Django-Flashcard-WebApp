from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class HomePage(View):
    template = 'home/home_page.html'

    def get(self, request):
        return render (request, self.template)

