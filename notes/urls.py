from django.urls import path
from notes.views import NotesListView, NoteDetailView, NoteDeleteView, NoteUpdateView, NoteCreateView

urlpatterns = [
    path('', NotesListView.as_view(), name='index'),
    path('add/', NoteCreateView.as_view(), name='create'),
    path('note/<int:pk>', NoteDetailView.as_view(), name='detail'),
    path('update/<int:pk>', NoteUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', NoteDeleteView.as_view(), name='delete')
]
