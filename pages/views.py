from django.shortcuts import render

def index(request):
    context = {
        'title': 'Школа японского языка SAKURANBO',
        'welcome_text': 'Ваше путешествие в мир Японского начинается здесь',
        'lead_text': 'Мы предлагаем самые уютные и качественные курсы японского языка. Здесь вы не просто выучите язык с нуля, но и найдете множество новых друзей.'
    }
    return render(request, 'pages/index.html', context)

def materials(request):
    context = {
        'title': 'Наши материалы',
    }
    return render(request, 'pages/materials.html', context)