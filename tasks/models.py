from django.db import models

from users.models import User


class AbstractTask(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('planned', 'Запланированная'),
        ('in progress', 'В работе'),
        ('completed', 'Завершенная'),
    ]
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание')
    creation_time = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Статус')
    deadline = models.DateField(db_index=True, verbose_name='Дата завершения')

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        ordering = ['-creation_time']


class Task(AbstractTask):
    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)
        TaskHistory.objects.create(
            task=self,
            user=self.user,
            title=self.title,
            description=self.description,
            status=self.status,
            deadline=self.deadline,
        )


class TaskHistory(AbstractTask):
    task = models.ForeignKey(Task, verbose_name='История изменений', related_name='change_history',
                             on_delete=models.CASCADE)
