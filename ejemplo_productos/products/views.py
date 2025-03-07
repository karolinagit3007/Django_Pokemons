from django.shortcuts import render, get_object_or_404
from .models import Pokemon

def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemon_list.html', {'pokemons': pokemons})

def pokemon_detail(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    return render(request, 'pokemon_detail.html', {'pokemon': pokemon})