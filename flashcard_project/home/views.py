from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from .models import Set, Card
from .forms import SetForm

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

class SetCreateView(View):
    template = 'home/set_create.html'

    def get(self, request):
        form = SetForm()
        ctx = {
            "form": form,
        }
        return render (request, self.template, ctx)
    
    def post(self, request):

        form = SetForm(request.POST)
        if form.is_valid():
            form.save()
        success_url = reverse_lazy('flashcard:sets_list')
        return redirect(success_url)