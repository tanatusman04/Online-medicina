from django.db import models

# Create your models here.


class Pill(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    amount = models.IntegerField(verbose_name='Количество')
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Лекарства"


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"