from django.db import models


class Event(models.Model):
    TICKET_TYPE_CHOICES = [
        ('VIP', 'VIP'),
        ('WITH_SPACE', 'With Space'),
        ('WITHOUT_SPACE', 'Without Space'),
        ('GROUP', 'Group'),
    ]

    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='event_images', blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    ticket_type = models.CharField(
        max_length=13,  # Increase to accommodate the longest choice
        choices=TICKET_TYPE_CHOICES,
        default='VIP',
    )

    def __str__(self):
        return f"{self.name} - {self.ticket_type}"



