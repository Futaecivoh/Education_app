from django.shortcuts import render
from .models import Course

def index(request):
    context = {
        'title': 'Школа японского языка SAKURANBO',
        'welcome_text': 'Ваше путешествие в мир Японского начинается здесь',
        'lead_text': 'Мы предлагаем самые уютные и качественные курсы японского языка. Здесь вы не просто выучите язык с нуля, но и найдете множество новых друзей.'
    }
    return render(request, 'pages/index.html', context)

def materials(request):
    courses = Course.objects.all()
    
    context = {
        'title': 'Наши курсы и материалы',
        'courses': courses,
    }
    return render(request, 'pages/materials.html', context)