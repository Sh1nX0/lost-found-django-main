from django.db import models
from django.utils import timezone

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
    location = models.CharField(max_length=200, blank=True, verbose_name="Место")
    contact_info = models.CharField(max_length=200, blank=True, verbose_name="Контакт")
    image = models.ImageField(upload_to='items/', blank=True, null=True, verbose_name="Изображение")
    date_created = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    
    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
    
    @property
    def found(self):
        """Свойство для совместимости"""
        return self.status == 'found'
    
    class Meta:
        ordering = ['-date_created']
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"