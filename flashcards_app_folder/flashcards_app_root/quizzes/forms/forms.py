from django import forms
from .models import Quiz

class AddQuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'num_questions']
        labels = {
            'title': 'Quiz Title',
            'num_questions': 'Number of Questions',
        }
