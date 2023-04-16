from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

# Register your models here.

class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name', 'first_name',)
    filter = ('email', 'user_name', 'first_name', 'address', 'is_active', 'is_staff')
    ordering = ('-date_joined',)
    list_display = ('email', 'user_name', 'first_name', 'last_name', 'contact', 'address', 'is_active', 'is_staff')
    # To eliminate field error
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'last_name', 'contact', 'address',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
        ('Personal', {'fields': ('about',)}),
    )

    formfield_overrides = {
        User.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'last_name', 'contact', 'address', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )


admin.site.register(User, UserAdminConfig)
