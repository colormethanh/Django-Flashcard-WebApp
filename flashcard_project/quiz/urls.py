from django.urls import path
from . import views

app_name = "quiz"

urlpatterns = [
    path("<slug:slug>", views.QuizView.as_view(), name="quiz_view")
]