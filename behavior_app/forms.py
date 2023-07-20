# behavior_app/forms.py
from django import forms
from .models import Note, Behavior


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['student', 'behavior', 'date', 'notes']


class BehaviorForm(forms.ModelForm):
    class Meta:
        model = Behavior
        fields = ['name']
