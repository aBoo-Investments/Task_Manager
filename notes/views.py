from django.template.response import TemplateResponse
from django.views.generic import ListView, DetailView, DeleteView

from notes.models import Note


def index(request, *args, **kwargs):
    return TemplateResponse(request, 'index.html')


class NotesListView(ListView):
    model = Note
    template_name = 'index.html'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'detail.html'

class NoteDeleteView(DeleteView):
    model = Note
    template_name_suffix = 'delete.html'