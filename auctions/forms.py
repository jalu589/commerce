from django import forms
from .models import Listing


class Listing_Form(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "description", "image", "category", "starting_price"]
        labels = {"title": "Name of item", "description": "Description", "image": "Image", "category": "Category", "starting_price": "Starting bid"}

