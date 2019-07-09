from django.views import generic
from client import models


class NoteView(generic.DetailView):
    model = models.Note
    template_name = 'client/note.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
