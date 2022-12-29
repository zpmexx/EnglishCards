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

# Create your views here.

