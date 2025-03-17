#urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_poke, name='all_poke'),  
    path('details/', views.all_poke, name='details'),  
]
