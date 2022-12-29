from django.forms import ModelForm
from django import forms
from .models import MemoryCard

class AddMemoryCardForm(ModelForm):
    
    class Meta:
        model = MemoryCard
        fields = ['polishName','englishName','polishDescription','englishDescription','wordLevel']
