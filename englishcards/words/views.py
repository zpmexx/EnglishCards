from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from logins.models import User
from django.contrib import messages
from .models import MemoryCard, Quiz, QuizElement, FavoriteUserCards
from .forms import AddMemoryCardForm
import random
from django.urls import reverse
from logins.views import home

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
        iterator = int(request.POST.get('iterator'))
        
        if iterator < 2:
            iterator = iterator +1
            quiz_element_obj= list(QuizElement.objects.filter(order = iterator))
            card = quiz_element_obj[0].memoryCard
            all_cards = list(FavoriteUserCards.objects.all())
            four_cards = [all_cards[0], all_cards[1], all_cards[2], card]
            random.shuffle(four_cards)
            context = {'four_cards':four_cards, 'iterator':iterator}
            return render(request, 'words/addQuiz.html', context) 
        else:
            return home(request)

    if request.method == 'GET':
        current_user = request.user
        quiz_obj = Quiz(user = current_user)
        quiz_obj.save()
        all_cards = list(FavoriteUserCards.objects.all())
        cards_to_learn = []
        for i in range(3):
            card_to_learn = random.choice(all_cards)
            index = all_cards.index(card_to_learn)
            all_cards.pop(index)
            cards_to_learn.append(card_to_learn) 
            quiz_element_obj = QuizElement(memoryCard = cards_to_learn[i], quiz = quiz_obj, order = i)
            quiz_element_obj.save()
        card = cards_to_learn[0]
        all_cards = list(FavoriteUserCards.objects.all())
        four_cards = [all_cards[0], all_cards[1], all_cards[2], card]
        random.shuffle(four_cards)
        context = {'four_cards':four_cards, 'iterator':0}
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
    return render(request, 'words/learnByLevel.html', context)
    

# Create your views here.

