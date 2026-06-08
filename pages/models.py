from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя тега")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена (в рублях)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", default=1)
    
    image = models.ImageField(upload_to='courses/', verbose_name="Изображение", blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='courses', verbose_name="Теги")

    def __str__(self):
        return f"{self.title} ({self.price} руб.)"
        
    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'pk': self.pk})