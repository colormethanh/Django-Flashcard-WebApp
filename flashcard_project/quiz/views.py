from django.shortcuts import render
from django.views import View
from home.models import Set, Card
from random import randint
from django.http import HttpResponse
# Create your views here.

# A funtion to choose a random card from the set
def getRandCard(cards):
    cardCT = len(cards)
    cardNum = randint(0, cardCT)

    return(cards[cardNum])




class QuizView(View):
    template = "quiz/quiz_form.html"

    def get(self, request, slug):
        setof = Set.objects.get(slug=slug)
        cards = Card.objects.filter(of_set=setof)
        ctx = {
            "setof":setof,
            "cards":cards 
        }
        return render(request, self.template, ctx )


