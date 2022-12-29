from django.contrib import admin
from .models import MemoryCard, QuizElement, Quiz

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
    list_display = ['memoryCard','wasCorrect','quiz']
    search_fields = ['memoryCard','wasCorrect','quiz']

class QuizAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user']


admin.site.register(MemoryCard, MemoryCardAdmin)
admin.site.register(QuizElement, QuizElementAdmin)
admin.site.register(Quiz, QuizAdmin)

# Register your models here.
