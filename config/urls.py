from django.contrib import admin
from django.urls import path, include
from pages.views import index, materials
from pages.views import index, materials, course_detail, contact_view, course_create, course_update, RegisterView, courses_by_tag
from django.contrib.auth.views import LoginView
from pages.forms import CustomLoginForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('', index, name='home'),
    path('', index, name='home'),
    path('materials/', materials, name='materials'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
    path('course/<int:pk>/edit/', course_update, name='course_detail'),
    path('contact/', contact_view, name='contact'),
    path('course/new/', course_create,name='course_create'),
    path('accounts/login/', LoginView.as_view(form_class=CustomLoginForm), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tag/<int:tag_id>/', courses_by_tag, name='courses_by_tag'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)