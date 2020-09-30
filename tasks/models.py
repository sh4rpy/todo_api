from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('planned', 'Запланированная'),
        ('in progress', 'В работе'),
        ('completed', 'Завершенная'),
    ]
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='user_tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание')
    creation_time = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Статус')
    deadline = models.DateField(db_index=True, verbose_name='Дата завершения')

    class Meta:
        ordering = ['-creation_time']
