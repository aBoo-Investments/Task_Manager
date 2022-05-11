from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Note, UserProfile


# Note update form
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['author','title', 'description', 'status']
        exclude = ['update']


# UserProfile update form
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'surname', 'age']
        exclude = ['update']


# User registration form
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        exclude = ['register']

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
