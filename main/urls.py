from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('thank_you', views.thank_you, name="thank_you"),
    path('uhguewljehug73', views.time_page, name="time"),
]