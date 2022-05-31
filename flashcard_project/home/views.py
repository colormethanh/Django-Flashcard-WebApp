from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Set, Card

# Create your views here.
class HomePage(View):
    template = 'home/home_page.html'

    def get(self, request):
        return render (request, self.template)

class SetsListView(View):
    template = 'home/sets_list.html'
    sets = Set.objects.all()

    ctx = {
        'sets':sets,
    }

    def get(self, request):
        return render (request, self.template, self.ctx)