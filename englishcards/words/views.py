from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from logins.models import User
from django.contrib import messages
from .models import MemoryCard, Quiz, QuizElement, FavoriteUserCards
from .forms import AddMemoryCardForm
import random

@login_required
def addWordPage(request):
    form = AddMemoryCardForm()
    if request.method == 'POST':
        form = AddMemoryCardForm(request.POST)
        if form.is_valid():
            if request.user.is_staff:
                form.save()
                messages.success(request,'Słówko dodane do bazy!', extra_tags='added_word')
            else:
                word = form.save(commit=False)
                word.confirmation_status = 1
                word.save()
                messages.success(request,'Słówko dodane do bazy oraz oczekuje na weryfikacje!', extra_tags='added_word')
            
    context = {'form':form}
    return render (request, 'words/addWord.html',context)


@login_required
def addQuizPage(request):
    if request.method == 'POST':
        pass
    current_user = request.user
    quiz_obj = Quiz(user = current_user)
    quiz_obj.save()
    all_cards = list(FavoriteUserCards.objects.all())
    cards_to_learn = []
    for i in range(10):
        cards_to_learn.append(random.choice(all_cards)) 
        quiz_element_obj = QuizElement(memoryCard = cards_to_learn[i], quiz = quiz_obj)
        quiz_element_obj.save()
    context = {'cards_to_learn' : cards_to_learn}
    return render(request, 'words/addQuiz.html', context)


def selectLevel(request):
    levels = ['A1','A2','B1','B2','C1','C2']
    context = {'levels': levels}
    return render(request, 'words/selectLevel.html', context)

def learnByLevel(request, slug):
    if slug == 'A1': level = 0
    elif slug == 'A2': level = 1
    elif slug == 'B1': level = 2
    elif slug == 'B2': level = 3
    elif slug == 'C1': level = 4
    elif slug == 'C2': level = 5
    words = list(MemoryCard.objects.filter(wordLevel = level))
    userWords = FavoriteUserCards.objects.filter(user = request.user)
    userWordsList = []
    for word in userWords:
        userWordsList.append(word.card)
        
    wordsToLearn = list(set(words) - set (userWordsList))
    wordToLearn = []
    if wordsToLearn:
        wordToLearn = random.choice(wordsToLearn)
    context = {'wordToLearn': wordToLearn}
    
    if request.method == 'POST':
        if 'next' in request.POST:
            pass
        else:
            counter = 1
            for arg in request.POST:
                if counter == 0:
                    counter = 1
                else:
                    cardId = arg
            card = MemoryCard.objects.get(id = cardId)
            print(card)
            favoriteCard = FavoriteUserCards.objects.create(user = request.user, card = card)
            favoriteCard.save()
    return render(request, 'words/fiszki.html', context)
    

# Create your views here.

