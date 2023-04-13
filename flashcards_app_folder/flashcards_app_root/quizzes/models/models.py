from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Question(models.Model):
    QUESTION_TYPES = (
        ('MC', 'Multiple Choice'),
        ('FB', 'Fill in the Blank'),
    )

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    content = models.TextField()
    answer = models.CharField(max_length=200)
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPES, default='MC')
    choices = models.TextField(blank=True, help_text="Enter choices separated by a comma (,) for multiple choice questions.")
