from django.contrib import admin
from django.urls import path
from pages.views import index, materials

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('materials/', materials, name='materials'),
]