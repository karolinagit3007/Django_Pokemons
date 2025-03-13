from django.shortcuts import render, get_object_or_404, redirect
from .models import Pokemon
from .forms import PokemonForm
from django.core.paginator import Paginator


def pokemon_create(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pokemon_list')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})

def pokemon_update(request,id):
    pokemon = get_object_or_404(Pokemon, id=id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokemon_list')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon_form.html', {'form': form})    

def pokemon_list(request):
    query = request.GET.get('q', '')  # Obtener el parámetro de búsqueda
    pokemons = Pokemon.objects.all()

    if query:
        pokemons = pokemons.filter(name__icontains=query)  # Filtrar por nombre

    # Paginación
    paginator = Paginator(pokemons, 6)  # 6 Pokémon por página
    page_number = request.GET.get('page')
    pokemons_page = paginator.get_page(page_number)

    return render(request, 'pokemon_list.html', {'pokemons': pokemons_page})

def pokemon_detail(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    return render(request, 'pokemon_detail.html', {'pokemon': pokemon})

def pokemon_delete(request, id):
    pokemon = get_object_or_404(Pokemon, id=id)
    pokemon.delete()
    return redirect('pokemon_list') 