"""englishcards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from logins import views as logins_views
from words import views as words_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', logins_views.home, name="home"),
    path('logowanie/', logins_views.loginPage, name = 'login'),
    path('rejestracja/', logins_views.registerPage, name = 'register'),
    path('wylogowanie/', logins_views.logoutPage, name = 'logout'),
    path('dodaj/', words_views.addWordPage, name = 'addWord'),
    path('nowy_quiz/', words_views.addQuizPage, name = 'addQuiz'),
    path('ulubione/', logins_views.userFavorites, name = 'userFavorites'),
    path('nauka/', words_views.selectLevel, name = 'selectLevel'),
    path('nauka/<slug:slug>/', words_views.learnByLevel, name = 'learnByLevel'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
