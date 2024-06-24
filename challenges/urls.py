from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("<int:month>", views.monthly_challenge_numbers),
    path("<str:month>", views.monthly_challenge, name="month-chalenge")    
]
