from django.db import models

class Item(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Потеряно'),
        ('found', 'Найдено'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        verbose_name='Статус'
    )
    location = models.CharField(max_length=200, verbose_name='Место')
    date = models.DateField(verbose_name='Дата')
    contact_info = models.CharField(max_length=200, verbose_name='Контактная информация')
    image = models.ImageField(
        upload_to='items/', 
        blank=True, 
        null=True, 
        verbose_name='Фото'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    def __str__(self):
        return f"{self.get_status_display()}: {self.title}"