from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена (в рублях)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.title} ({self.price} руб.)"
        
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"