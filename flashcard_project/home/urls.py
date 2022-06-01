from django.urls import path
from . import views

app_name = "flashcard"

urlpatterns = [
    path("", views.HomePage.as_view(), name="home_page"),
    path("sets", views.SetsListView.as_view(), name="sets_list"),
    path("set_create", views.SetCreateView.as_view(), name="set_create"),
]