from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Form for adding a new topic."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.TextInput(attrs={'placeholder': 'Enter topic here'})}

class EntryForm(forms.ModelForm):
    """Form for adding a new entry."""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}