from django.db import models
from logins.models import User

# Create your models here.

english_level = [
    (0, ("A1")),
    (1, ("A2")),
    (2, ("B1")),
    (3, ("B2")),
    (4, ("C1")),
    (5, ("C2")),
]


confirmation_status = [
    (0, ("zatwierdzone")),
    (1, ("niezatwierdzone")),
]



class MemoryCard(models.Model):
    polishName = models.CharField(verbose_name="Polskie słowo", blank=False, null=False, default = "defaultpolishword", max_length=50)
    englishName = models.CharField(verbose_name="Angielskie słowo", blank=False, null=False, default = "defaultenglishword", max_length=50)
    polishDescription = models.TextField(verbose_name="Polski opis", blank=False, null=False, default = "defaultpolishdescription", max_length=500)
    englishDescription = models.TextField(verbose_name="Angielski opis", blank=False, null=False, default = "defaultenglishdescription", max_length=500)
    wordLevel = models.IntegerField(choices=english_level, default=0, verbose_name='Poziom słówka')
    confirmation_status = models.IntegerField(choices=confirmation_status, default=0, verbose_name='Status')

    def __str__(self):
        return str(f'{self.englishName},{self.polishName}')

    class Meta:
        verbose_name = "Słówko"
        verbose_name_plural = "Słówka"
        
        
class FavoriteUserCards(models.Model):
    user = models.ForeignKey(User, verbose_name="Użytkownik",on_delete=models.CASCADE)
    card = models.ForeignKey(MemoryCard, verbose_name="Karta",on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.user.username},{self.card.englishName},{self.card.polishName}')
    
    class Meta:
        verbose_name = "Ulubiona karta"
        verbose_name_plural = "Ulubione karty"
        

class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)




class QuizElement(models.Model):
    memoryCard = models.ForeignKey(FavoriteUserCards, on_delete=models.DO_NOTHING)
    wasCorrect = models.BooleanField(verbose_name="Poprawność odpowiedzi", blank=True, null=True, default = False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)