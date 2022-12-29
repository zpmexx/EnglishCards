from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import MemoryCard
from .forms import AddMemoryCardForm

@login_required
def addWordPage(request):
    form = AddMemoryCardForm()
    if request.method == 'POST':
        pass
    context = {'form':form}
    return render (request, 'words/addWord.html',context)

@login_required
def learnFromCardsPage(request):
    cards = MemoryCard.objects.all()
    context={'cards':cards}
    return render (request, 'words/fiszki.html', context)

# Create your views here.

