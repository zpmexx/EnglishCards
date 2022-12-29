from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from logins.models import User

from .models import MemoryCard, Quiz, QuizElement
from .forms import AddMemoryCardForm

@login_required
def addWordPage(request):
    form = AddMemoryCardForm()
    if request.method == 'POST':
        pass
    context = {'form':form}
    return render (request, 'words/addWord.html',context)


@login_required
def addQuizPage(request):
    if request.method == 'POST':
        pass
    current_user = request.user
    quiz_obj = Quiz(user = current_user)
    quiz_obj.save()
    cards = MemoryCard.objects.all()
    for card in cards:
        quiz_element_obj = QuizElement(memoryCard = card, quiz = quiz_obj)
        quiz_element_obj.save()
    quiz_elements = QuizElement.objects.filter(quiz = quiz_obj)
    context = {'quiz_elements' : quiz_elements}
    return render(request, 'words/addQuiz.html', context)


# Create your views here.

