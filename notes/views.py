from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from notes.forms import NoteForm, NewUserForm, UserProfileForm
from notes.models import Note, UserProfile


# List views to front-end application
class NotesListView(ListView):
    model = Note
    template_name = 'index.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Note.objects.filter(author=self.request.user.id)


# Note detail view
class NoteDetailView(DetailView):
    model = Note
    template_name = 'detail.html'


# Note update view
class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'update.html'
    form_class = NoteForm
    success_url = '/'


# Note update view
class UserProfileUpdateView(UpdateView):
    model = UserProfile
    template_name = 'registration/user-update.html'
    form_class = UserProfileForm
    success_url = '/'


# Note delete view
class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'delete.html'
    success_url = reverse_lazy('index')


# Note create  view
class NoteCreateView(CreateView, LoginRequiredMixin):
    model = Note
    template_name = 'create.html'
    form_class = NoteForm
    success_url = reverse_lazy('index')


# Application login confirmation
def login_success(request):
    return TemplateResponse(request, 'registration/login-success.html')


# Application registration
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/registration.html", context={"register_form": form})
