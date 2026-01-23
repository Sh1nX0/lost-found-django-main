from django.db import models

class Item(models.Model):
    # Тип: потерян или найден
    ITEM_TYPE = [
        ('lost', 'Потерян'),
        ('found', 'Найден'),
    ]
    
    type = models.CharField(max_length=10, choices=ITEM_TYPE, verbose_name='Тип')
    name = models.CharField(max_length=200, verbose_name='Название предмета')
    description = models.TextField(verbose_name='Описание')
    location = models.CharField(max_length=200, verbose_name='Место')
    date = models.DateField(verbose_name='Дата')
    contact = models.CharField(max_length=100, verbose_name='Контакт')
    image = models.ImageField(upload_to='items/', blank=True, null=True, verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    def __str__(self):
        return f"{self.get_type_display()}: {self.name}"