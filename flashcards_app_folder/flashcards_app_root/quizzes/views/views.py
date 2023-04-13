from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from ..models.models import Quiz, Question
from .forms import AddQuizForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('quizzes')
        else:
            return render(request, 'quizzes/login.html', {'error': 'Invalid username or password'})
    return render(request, 'quizzes/login.html')

@login_required
def quizzes(request):
    user_quizzes = Quiz.objects.filter(user=request.user)
    return render(request, 'quizzes/quizzes.html', {'quizzes': user_quizzes})

@login_required
def add_quiz(request):
    if request.method == 'POST':
        title = request.POST['title']
        quiz = Quiz.objects.create(user=request.user, title=title)

        num_questions = int(request.POST['num_questions'])

        for i in range(num_questions):
            content = request.POST.get(f'question_content_{i+1}', '')
            answer = request.POST.get(f'question_answer_{i+1}', '')
            question_type = request.POST.get(f'question_type_{i+1}', 'MC')
            choices = request.POST.get(f'question_choices_{i+1}', '')

            Question.objects.create(
                quiz=quiz,
                content=content,
                answer=answer,
                question_type=question_type,
                choices=choices
            )

        return redirect('quizzes')
    return render(request, 'quizzes/add_quiz.html')

@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, user=request.user)
    questions = quiz.question_set.all()
    return render(request, 'quizzes/quiz_detail.html', {'quiz': quiz, 'questions': questions})

def homepage(request):
    return redirect('login')

def add_quiz(request):
    if request.method == 'POST':
        form = AddQuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.user = request.user
            quiz.save()
            # Redirect to the new quiz's detail page
            return redirect('quiz_detail', quiz_id=quiz.id)
    else:
        form = AddQuizForm()

    return render(request, 'quizzes/add_quiz.html', {'form': form})