from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.user_login, name='login'),
    path('quizzes/', views.quizzes, name='quizzes'),
    path('add_quiz/', views.add_quiz, name='add_quiz'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail')
]
