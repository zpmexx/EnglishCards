from django.contrib import admin
from .models import MemoryCard

class MemoryCardAdmin(admin.ModelAdmin):
    list_display = ['englishName','polishName','wordLevel','confirmation_status']
    search_fields = ['englishName',' polishName','wordLevel','confirmation_status']
    ordering = ['englishName','polishName']
    list_filter = ['wordLevel','confirmation_status']
    
    fieldsets = (
        ('Szczegóły słowa', {'fields': ('englishName','englishDescription','polishName','polishDescription','wordLevel')}),
        ('Status', {'fields': ('confirmation_status',)}),
    )

admin.site.register(MemoryCard, MemoryCardAdmin)
# Register your models here.
