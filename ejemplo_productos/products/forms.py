from django import forms
from django.core.exceptions import ValidationError
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = [
            "name",
            "type",
            "image",
            "abilities",
            "height",
            "weight",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "type": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.URLInput(attrs={"class": "form-control"}),
            "abilities": forms.Textarea(attrs={"class": "form-control"}),
            "height": forms.NumberInput(attrs={"class": "form-control"}),
            "weight": forms.NumberInput(attrs={"class": "form-control"}),
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        if not name.isalpha():
            raise ValidationError("El nombre debe contener solo letras.")
        return name