from django.contrib import messages
from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from notes.forms import NoteForm, NewUserForm
from notes.models import Note


class NotesListView(ListView):
    model = Note
    template_name = 'index.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Note.objects.all()


class NoteDetailView(DetailView):
    model = Note
    template_name = 'detail.html'


class NoteUpdateView(UpdateView, SuccessMessageMixin):
    model = Note
    template_name = 'update.html'
    form_class = NoteForm
    success_message = '%(title)s was created successfully'
    success_url = '/'


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'delete.html'
    success_url = reverse_lazy('index')


class NoteCreateView(CreateView, SuccessMessageMixin):
    model = Note
    template_name = 'create.html'
    form_class = NoteForm
    success_url = reverse_lazy('index')
    success_message = '%(title)s was created successfully'


def login_success(request):
    return TemplateResponse(request, 'registration/login-success.html')


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
