from django.forms import ModelForm
from django import forms
from .models import MemoryCard, QuizElement

class AddMemoryCardForm(ModelForm):

    class Meta:
        model = MemoryCard
        fields = ['polishName','englishName','polishDescription','englishDescription','wordLevel']

class AddQuizForm(ModelForm):
    
    class Meta:
        model = QuizElement
        fields = ['memoryCard']