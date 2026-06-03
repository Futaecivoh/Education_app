from django.contrib import admin
from django.urls import path
from pages.views import index, materials
from pages.views import index, materials, course_detail, contact_view, course_create, course_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('materials/', materials, name='materials'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
    path('course/<int:pk>/edit/', course_update, name='course_detail'),
    path('contact/', contact_view, name='contact'),
    path('course/new/', course_create,name='course_create'),
]