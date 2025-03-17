# foody/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.recepies_view, name='foody'), 
    path('recepies/', views.recepies_view, name='recepies'),  
    path('delete-recepies/<id>/', views.delete_recepie, name='delete-recepies'),  
    path('update-recepies/<id>/', views.update_recepie, name='delete-recepies'),  


]
