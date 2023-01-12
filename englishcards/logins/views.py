from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterUserForm
from django.contrib import messages
from words.models import MemoryCard, FavoriteUserCards
from django.core.paginator import Paginator
import random
# Create your views here.

def home(request):
    cards = list(MemoryCard.objects.all())
    dailyWords = random.sample(cards, 3)
    context = {'dailyWords' : dailyWords}
    return render (request, 'logins/home.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username,password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Niepoprawne dane logowania', extra_tags='bad_credentials')
            
    context = {}
    return render (request, 'logins/login.html',context)


def registerPage(request):
    form = RegisterUserForm()
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Stworzono konto dla ' + user, extra_tags='singup')
            return redirect('login')
        else:
            messages.info(request,'Błedne dane rejestracji', extra_tags='bad_register_credentials')
    context = {'form':form}
    return render (request, 'logins/register.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def userFavorites(request):
    
    iterator = 0
    if request.method == 'POST':
        for arg in request.POST:
            if iterator == 0:
                iterator = 1
            else:
                word = arg
        englishWord, polishWord = word.split(',')
        FavoriteUserCards.objects.filter(user = request.user, card__englishName = englishWord, card__polishName = polishWord).delete()
    
    favoriteCards = FavoriteUserCards.objects.filter(user = request.user)
    paginator = Paginator(favoriteCards, 3)
    page_number = request.GET.get("page")
    favoriteCards = paginator.get_page(page_number)
    context = {'favoriteCards': favoriteCards}
    
    return render (request, 'logins/userfavorites.html',context)