from django.urls import path
from . import views # imports views to connect routes to view functions

urlpatterns = [
  #Routes will be added here 
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
]