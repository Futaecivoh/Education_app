from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import FeedbackForm

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
    
    context ={
        'title': course.title,
        'course': course,
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