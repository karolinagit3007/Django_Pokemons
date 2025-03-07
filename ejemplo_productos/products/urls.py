from django.urls import path
from .views import pokemon_list, pokemon_detail  # Asegúrate de importar ambas vistas

urlpatterns = [
    path('', pokemon_list, name='pokemon_list'),
    path('pokemon/<int:id>/', pokemon_detail, name='pokemon_detail'),
]