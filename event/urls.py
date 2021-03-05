from django.urls import path
from . import views

urlpatterns = [
    path('events/',views.events,	name='events'),
    path('events/e-summit/',views.esummit,name='esummit'),
    path('events/venture-lab/',views.vl,name='vl'),
    path('events/startup-weekend/',views.starteco,name='startupweekend'),
    path('events/e-talks/1/',views.etalk,name='etalks'),
    path('events/e-talks/2/',views.etalk2,name='etalks2'),
]
