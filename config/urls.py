from django.contrib import admin
from django.urls import path
from pages.views import index, materials
from pages.views import index, materials, course_detail, contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('materials/', materials, name='materials'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
    path('contact/', contact_view, name='contact'),
]