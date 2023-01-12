from django.forms import ModelForm
from django import forms
from .models import MemoryCard, QuizElement

class AddMemoryCardForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(AddMemoryCardForm, self).__init__(*args, **kwargs)
        
        self.fields['polishName'].initial = ''
        self.fields['englishName'].initial = ''
        self.fields['polishDescription'].initial = ''
        self.fields['englishDescription'].initial = ''
        
    class Meta:
        model = MemoryCard
        fields = ['polishName','englishName','polishDescription','englishDescription','wordLevel']
        
        widgets = {
            'polishName': forms.TextInput(attrs={'placeholder': 'Polskie słówko'}),
             'englishName': forms.TextInput(attrs={'placeholder': 'English word'}),
        }

class AddQuizForm(ModelForm):
    
    class Meta:
        model = QuizElement
        fields = ['card']