from django import forms

from .models import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ["name", "category", "description", "lat", "lng"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Place name"}),
            "category": forms.TextInput(attrs={"placeholder": "Category"}),
            "description": forms.Textarea(
                attrs={"placeholder": "Description", "rows": 3}
            ),
            "lat": forms.NumberInput(
                attrs={"placeholder": "Latitude", "step": "any", "min": -90, "max": 90}
            ),
            "lng": forms.NumberInput(
                attrs={
                    "placeholder": "Longitude",
                    "step": "any",
                    "min": -180,
                    "max": 180,
                }
            ),
        }
