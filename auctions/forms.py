from fileinput import FileInput
from django import forms
from .models import Listing, Bid


class Listing_Form(forms.ModelForm):
    class Meta:
        model = Listing 
        fields = "__all__"


class Bid_Form(forms.ModelForm):
    class Meta:
        model = Bid
        fields = "__all__"
