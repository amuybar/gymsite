from django.db import models

"""
Manages gym equipment inventory and maintenance.
"""

class Equipment(models.Model):
    STATUS=[
        ('UM','under maintenance'),
        ('A','Available')
    ]
    name=models.CharField(max_length=100)
    status=models.CharField(max_length=30,choices=STATUS)
    last_maintenance=models.DateTimeField()
    next_maintenance=models.DateTimeField()