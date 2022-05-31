from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path("", views.HomePage.as_view(), name="home_page"),
    path("sets", views.SetsListView.as_view(), name="sets_list")
]