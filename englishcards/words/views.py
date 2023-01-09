from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from logins.models import User
from django.contrib import messages
from .models import MemoryCard, Quiz, QuizElement, FavoriteUserCards
from .forms import AddMemoryCardForm
import random
from django.urls import reverse
from logins.views import home
from django.db.models import Q
import json
import datetime

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
        
        card_id, iterator, quiz_id = json.loads(request.POST.get('answer_button'))
        iterator = int(iterator)
        quiz = Quiz.objects.filter(id = quiz_id)
        answer_card = list(QuizElement.objects.filter(order = iterator, quiz = quiz[0]))
        print(answer_card)
        if int(answer_card[0].card.id) == int(card_id):
            print("correct")
            answer_card[0].wasCorrect = True      
            answer_card[0].card.score = answer_card[0].card.score +1
            answer_card[0].card.save()
            answer_card[0].save()
        else:
            print("not correct")
            answer_card[0].wasCorrect = False
            answer_card[0].card.score = answer_card[0].card.score - 1
            answer_card[0].card.save()
            answer_card[0].save()
        if iterator < 9:
            iterator= iterator+1
            next_card= list(QuizElement.objects.filter(order = iterator, quiz = quiz[0]))
            card = next_card[0].card
            all_cards = list(FavoriteUserCards.objects.all().exclude(card=card.card))
            four_cards = [all_cards[0], all_cards[1], all_cards[2], card]
            random.shuffle(four_cards)
            context = {'four_cards':four_cards, 'iterator':iterator, 'card':card, 'quiz_id':quiz_id}
            return render(request, 'words/addQuiz.html', context)
        else:
            result = list(QuizElement.objects.filter(quiz = quiz[0]))
            points = QuizElement.objects.filter(quiz = quiz[0], wasCorrect = True).count()
            quiz_obj = quiz[0]
            quiz_obj.points = points
            quiz_obj.date = datetime.datetime.now()
            quiz_obj.save()
            context = {'cards':result, 'points':points}
            return render(request, 'words/resultQuiz.html', context)
    if request.method == 'GET':
        quiz_obj = Quiz(user = request.user)
        quiz_obj.save()
        quiz_id = quiz_obj.pk
        print(quiz_id)
        all_cards = list(FavoriteUserCards.objects.all().order_by('score'))
        cards_to_learn = []
        print(all_cards)
        for i in range(5):
            card_to_learn = all_cards[0]
            index = all_cards.index(card_to_learn)
            all_cards.pop(index)
            cards_to_learn.append(card_to_learn) 
            quiz_element_obj = QuizElement(card= cards_to_learn[i], quiz = quiz_obj, order = i)
            quiz_element_obj.save()

        for i in range(5):
            card_to_learn = random.choice(all_cards)
            index = all_cards.index(card_to_learn)
            all_cards.pop(index)
            cards_to_learn.append(card_to_learn) 
            quiz_element_obj = QuizElement(card= cards_to_learn[i+5], quiz = quiz_obj, order = i+5)
            quiz_element_obj.save()
        print(cards_to_learn)
        card = cards_to_learn[0]
        all_cards = list(FavoriteUserCards.objects.all().exclude(card=card.card))     
        four_cards = [all_cards[0], all_cards[1], all_cards[2], card]
        random.shuffle(four_cards)
        context = {'four_cards':four_cards, 'iterator':0,  'card':card , 'quiz_id':quiz_id}
        return render(request, 'words/addQuiz.html', context) 

@login_required
def quizHistory(request):
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        quizzes = Quiz.objects.filter(user=request.user) 
        context = {'quizzes':quizzes}
        return render(request, 'words/quizHistory.html', context)
        
def quizDetails(request, quiz_id):
    if request.method == 'POST':
        pass
    if request.method == 'GET':
        quiz = Quiz.objects.get(id=quiz_id)
        quiz_elements = QuizElement.objects.filter(quiz=quiz).order_by('order')
        context = {'quiz': quiz, 'quiz_elements': quiz_elements}
        return render(request, 'words/quizDetails.html', context)


def selectLevel(request):
    levels = ['A1','A2','B1','B2','C1','C2']
    context = {'levels': levels}
    return render(request, 'words/selectLevel.html', context)

def learnByLevel(request, slug):
    
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
            # if card in wordsToLearn:
            #     wordsToLearn.remove(card)
            favoriteCard = FavoriteUserCards.objects.create(user = request.user, card = card)
            favoriteCard.save()
    
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
    
    print(userWordsList)    
    wordsToLearn = list(set(words) - set (userWordsList))
    print(wordsToLearn)
    wordToLearn = []
    if wordsToLearn:
        wordToLearn = random.choice(wordsToLearn)
    context = {'wordToLearn': wordToLearn}
    

    return render(request, 'words/fiszki.html', context)
    

def findCard(request):
    context = {}
    if request.method == 'POST':
        searchCard = request.POST.get('findCard')
        card = MemoryCard.objects.filter(Q(englishName__iexact = searchCard) | Q(polishName__iexact = searchCard)).first()
        if not card:
            message = 'Brak słówka w bazie danych!'
            context = {'message': message}
        else:
            context = {'card': card}
    return render(request, 'words/findCard.html', context)

# Create your views here.

