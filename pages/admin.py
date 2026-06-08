from django.contrib import admin
from .models import Course, Tag

admin.site.register(Tag)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')
    search_fields = ('title',)