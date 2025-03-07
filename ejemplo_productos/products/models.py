from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=255)  # Nombre del Pokémon
    type = models.CharField(max_length=255)  # Tipo de Pokémon (por ejemplo, "Agua", "Fuego")
    image = models.URLField()  # URL de la imagen del Pokémon
    abilities = models.TextField()  # Habilidades del Pokémon
    height = models.DecimalField(decimal_places=2, max_digits=10)  # Altura del Pokémon
    weight = models.DecimalField(decimal_places=2, max_digits=10)  # Peso del Pokémon

    def __str__(self):
        return self.name