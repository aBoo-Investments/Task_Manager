from django.contrib import admin
from .models import UserProfile, Note


@admin.register(UserProfile)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'surname', 'age']


@admin.register(Note)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['title', 'color']
