from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from notes.forms import NoteForm
from notes.models import Note


class NotesListView(ListView):
    model = Note
    template_name = 'index.html'


class NoteDetailView(DetailView):
    model = Note
    template_name = 'detail.html'


class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'update.html'
    form_class = NoteForm
    success_url = "/"


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'delete.html'
    success_url = reverse_lazy('index')


class NoteCreateView(CreateView):
    model = Note
    template_name = 'create.html'
    form_class = NoteForm
    success_url = reverse_lazy('index')
