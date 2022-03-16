from django import forms
from .models import TechType, movie, Review

class MovieForm(forms.ModelForm):
    class Meta:
        model=movie
        fields='__all__'