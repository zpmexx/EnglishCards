from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class UserAdmins(UserAdmin):
    list_display = ['username','first_name','last_name','email','phone_number']
    search_fields = ['username','first_name','last_name','email','phone_number']
    ordering = ['last_name','first_name','username']
    readonly_fields = ['date_joined']
    
    fieldsets = (
        ('Informacje o użytkowniku', {'fields': ('username','password','date_joined')}),
        ('Personalia', {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        ('Uprawnienia', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    
    
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets

        # staff user to be able to edit
        if request.user.is_superuser:
            perm_fields = ('is_active', 'is_staff', 'is_superuser',
                        'groups', 'user_permissions')
        else:
            # modify these to suit the fields you want your
            perm_fields = ('is_active', 'is_staff')

        return (
            ('Informacje o użytkowniku', {'fields': ('username','password','date_joined')}),
            ('Personalia', {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
            ('Uprawnienia', {'fields': perm_fields}),
    )
    
admin.site.register(User, UserAdmins)
admin.site.site_header = 'Panel administracyjny English Cards'