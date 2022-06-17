from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from .models import Set, Card
from .forms import SetForm, CardForm

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
    template = 'home/create_form.html'

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

class SetDetailView(View):
    template = 'home/set_detail.html'

    def get(self, request, slug):

        current_set = Set.objects.get(slug = slug)

        cards = Card.objects.filter(of_set = current_set)

        return render(request, self.template, {"slug": slug, "cards":cards })

class CardCreateView(View):
    template = 'home/create_form.html'

    def get(self, request, slug):
        form = CardForm()
        ctx = {
            "form": form
        }
        return render (request, self.template, ctx)

    def post(self, request, slug):
        form = CardForm(request.POST)
        current_set = Set.objects.get(slug = slug)

        if form.is_valid():
            card = form.save(commit=False)
            card.of_set = current_set
            form.save()
        success_url = reverse_lazy('flashcard:set_detail', kwargs={"slug":slug})
        return redirect(success_url)

