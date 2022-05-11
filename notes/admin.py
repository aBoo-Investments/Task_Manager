from django.contrib import admin
from .models import UserProfile, Note


# Model display in Django administration
@admin.register(UserProfile)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'surname', 'age']


# Model display in Django administration
@admin.register(Note)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created', 'modified']
