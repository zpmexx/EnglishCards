from django.contrib import admin
from .models import MemoryCard, QuizElement, Quiz, FavoriteUserCards

class MemoryCardAdmin(admin.ModelAdmin):
    list_display = ['englishName','polishName','wordLevel','confirmation_status']
    search_fields = ['englishName',' polishName','wordLevel','confirmation_status']
    ordering = ['englishName','polishName']
    list_filter = ['wordLevel','confirmation_status']
    
    fieldsets = (
        ('Szczegóły słowa', {'fields': ('englishName','englishDescription','polishName','polishDescription','wordLevel')}),
        ('Status', {'fields': ('confirmation_status',)}),
    )

class QuizElementAdmin(admin.ModelAdmin):
    list_display = ['card','wasCorrect','quiz']
    search_fields = ['card','wasCorrect','quiz']

class QuizAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user']

class FavoriteUserCardsAdmin(admin.ModelAdmin):
    list_display = ['user','card','get_wordlLevel', 'id', 'score']
    
    def get_wordlLevel(self, obj):
        return obj.card.get_wordLevel_display()
    get_wordlLevel.admin_order_field  = 'card__wordLevel' 
    get_wordlLevel.short_description = 'Wordl level'  

admin.site.register(MemoryCard, MemoryCardAdmin)
admin.site.register(QuizElement, QuizElementAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(FavoriteUserCards, FavoriteUserCardsAdmin)

# Register your models here.
