from django.urls import path
from . import views

urlpatterns = [
    path('', views.Lucario, name='lucario'),  
    path('lucarioss/', views.Lucario, name='lucarioss'), 
]
