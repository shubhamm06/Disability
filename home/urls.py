from django.urls import path
from . import views

urlpatterns = [
    path('',			views.home,		name='home'),
    path('our-team/',	views.team,		name='our-team'),
    path('tech-team/',	views.techteam,	name='tech-team'),
    path('partners/',	views.sponsor,	name='sponsor'),
]
