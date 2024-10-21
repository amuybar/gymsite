from tkinter.constants import CASCADE

from django.db import models
from core.models import ContactInfo
"""
 This model classes manage all aspects related to gym members,
 their information,
  and their membership details.
"""
class MemberShipType(models.Model):
    """
    Membership Type class handles the various membership subscription plan
    with their prices and duration for each day
    strict the membership choices to annually,monthly or weekly
    """
    MEMBER_CHOICES=[
        ('A', 'Annually'),
        ('M','Monthly'),
        ('W','Weekly'),
    ]
    name = models.CharField(max_length=50,choices=MEMBER_CHOICES)
    price = models.IntegerField()
    duration_in_days = models.IntegerField()

    def __str__(self):
        return self.name


class Member(ContactInfo):
    membership_start_date=models.DateField()
    membership_end_date=models.DateField()
    membership_type=models.ForeignKey(MemberShipType,on_delete=models.CASCADE)
    status=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


