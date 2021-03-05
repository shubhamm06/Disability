from django.urls import path
from . import views
from .views import InvestorCreateView, InvestorDeleteView, InvestorUpdateView, Startup

urlpatterns = [
    path('investors/', views.Investors, name='investors'),
    path('investors/create/', views.InvestorCreateView, name='investor-create'),
    path('investors/<int:pk>/delete/', InvestorDeleteView.as_view(), name='investor-delete'),
    path('investors/<int:pk>/update/', InvestorUpdateView, name='investor-update'),
    path('startup/', views.Startup, name='startup'),
	]