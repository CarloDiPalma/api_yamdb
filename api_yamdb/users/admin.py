from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'role', 'bio')
    list_editable = ('role',)
    search_fields = ('username',)
    empty_value_display = '-пусто-'
