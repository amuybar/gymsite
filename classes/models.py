from django.db import models

from members.models import Member
from trainers.models import Trainer

"""
Manages class schedules, bookings, and attendance
"""

class ClassSchedule(models.Model):
    class_name=models.CharField(max_length=100)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    capacity=models.IntegerField()
    Trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    day_of_week=models.CharField(max_length=30)

    def __str__(self):
        return self.class_name

class Booking(models.Model):
    class_booked=models.ForeignKey(ClassSchedule,on_delete=models.CASCADE)
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    booking_date=models.DateTimeField()

class Attendance(models.Model):
    STATUS_CHOICE=[
        ('P','Present'),
        ('A','Absent')
    ]
    class_attended = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    attendance_date = models.DateTimeField()
    status=models.CharField(max_length=30,choices=STATUS_CHOICE)
