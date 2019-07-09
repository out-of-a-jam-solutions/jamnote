from django.urls import path
from client import views


urlpatterns = [
    path('<uuid:id>', views.NoteView.as_view(), name='note'),
]
