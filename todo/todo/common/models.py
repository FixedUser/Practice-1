from django.db import models


class Task(models.Model):
    LOW = 'LOW'
    MID = 'MIDDLE'
    HIGH = 'HIGH'
    PRIORITY_ENUM = [
        (LOW, 'Low'),
        (MID, 'Middle'),
        (HIGH, 'High')
    ]
    title = models.CharField(max_length=100)
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_ENUM,
        default=LOW,
        verbose_name='Priority'
    )
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Task "{self.title}" with priority {self.priority}'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('task_list')