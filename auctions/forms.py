from fileinput import FileInput
from django import forms
from .models import Listing


class Listing_Form(forms.ModelForm):
    class Meta:
        model = Listing 
        fields = "__all__"

