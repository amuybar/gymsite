from django.db import models

from core.models import ContactInfo


class Trainer(ContactInfo):
    AVAILABLE=[
        ('A','Available'),
        ('N', 'Not Available')
    ]
    hourly_rate=models.IntegerField()
    specialization=models.CharField(max_length=40)
    certification=models.CharField(max_length=30)
    availability=models.CharField(max_length=30,choices=AVAILABLE)