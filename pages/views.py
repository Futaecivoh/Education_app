from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import FeedbackForm, CourseForm,CustomRegisterForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Course, Tag
from django.contrib import messages

def courses_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    courses = tag.courses.all()
    
    context = {
        'title': f'Курсы по тегу: {tag.name}',
        'courses': courses,
    }
    return render(request, 'pages/materials.html', context)

def index(request):
    context = {
        'title': 'Школа японского языка SAKURANBO',
        'welcome_text': 'Ваше путешествие в мир Японского начинается здесь',
        'lead_text': 'Мы предлагаем самые уютные и качественные курсы японского языка. Здесь вы не просто выучите язык с нуля, но и найдете множество новых друзей.'
    }
    return render(request, 'pages/index.html', context)
pass

def materials(request):
    courses = Course.objects.all()
    
    context = {
        'title': 'Наши курсы и материалы',
        'courses': courses,
    }
    return render(request, 'pages/materials.html', context)
pass

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    comment_form = CommentForm()
    
    context = {
        'title': course.title,
        'course': course,
        'comment_form': comment_form
    }
    return render(request, 'pages/course_detail.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        
        if form.is_valid():
            print("=== НОВОЕ СООБЩЕНИЕ ===")
            print(form.cleaned_data)
            print("=======================")
            
            return redirect('home')
            
    else:
        form = FeedbackForm()

    context = {
        'title': 'Обратная связь',
        'form': form
    }
    return render(request, 'pages/contact.html', context)

@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.author = request.user
            course.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm()
    context = {'form': form, 'title': 'Добавление нового курса'}
    return render(request, 'pages/course_form.html', context)

@login_required
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST, request.FILES, instance=course)
    if form.is_valid():
        form.save()
        return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm(instance=course)
    
    context = {'form':form, 'title': 'Редактирование курса'}
    return render(request,'pages/course_form.html', context)

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomRegisterForm
    success_url = reverse_lazy('login')

@login_required
def add_comment(request, pk):
    course = get_object_or_404(Course, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.course = course
            comment.author = request.user
            comment.save()
            messages.success(request, 'Ваш комментарий успешно добавлен!')
        else:
            messages.error(request, 'Произошла ошибка при добавлении комментария.')
            
    return redirect('course_detail', pk=pk)