from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    event_type = models.CharField(max_length=10, choices=EVENT_TYPE_CHOICES)
    max_seats = models.PositiveIntegerField()
    booking_open = models.BooleanField(default=False)
    booking_start_date = models.DateTimeField(null=True, blank=True)
    booking_end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.event.title}'
