#views.py
from django.shortcuts import render

# Create your views here.
def all_poke(request):
    return render(request, 'website/pokemonall.html')

