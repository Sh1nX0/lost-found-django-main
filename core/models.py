from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Location(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"

class Item(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Потеряно'),
        ('found', 'Найдено'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='lost',
        verbose_name="Статус"
    )
    
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name="Категория"
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Местоположение"
    )
    
    contact_info = models.CharField(max_length=200, blank=True, verbose_name="Контакт")
    date_created = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    
    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
    
    @property
    def found(self):
        return self.status == 'found'
    
    class Meta:
        ordering = ['-date_created']
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"