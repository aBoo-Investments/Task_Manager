from django.urls import path, include
from notes.views import NotesListView, NoteDetailView, NoteDeleteView, NoteUpdateView, NoteCreateView, login_success

urlpatterns = [
    path('', NotesListView.as_view(), name='index'),
    path('add/', NoteCreateView.as_view(), name='create'),
    path('note/<int:pk>', NoteDetailView.as_view(), name='detail'),
    path('update/<int:pk>', NoteUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', NoteDeleteView.as_view(), name='delete'),
    path('accounts/', include("django.contrib.auth.urls"), name='login'),
    path('accounts/', include("django.contrib.auth.urls"), name='logout'),
    path('accounts/', include("django.contrib.auth.urls"), name='login-success'),
    path('login-success', login_success, name='login-success'),
]
