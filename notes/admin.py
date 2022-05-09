from django.contrib import admin
from .models import UserProfile, Note


@admin.register(UserProfile)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Note)
class AuthorAdmin(admin.ModelAdmin):
    pass
