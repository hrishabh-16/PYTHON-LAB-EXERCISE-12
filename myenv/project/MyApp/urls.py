from django.urls import path
from . import views

urlpatterns = [
    path('election-registration/', views.election_registration, name='election_registration'),
]
