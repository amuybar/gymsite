from django.db import models

from members.models import Member, MemberShipType

"""
Handles all membership and training-related payments.
"""
class Payment(models.Model):
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    amount=models.IntegerField()
    payment_date=models.DateTimeField()
    payment_method=models.CharField(max_length=100)
    membership_type=models.ForeignKey(MemberShipType,on_delete=models.CASCADE)

    def __str__(self):
        return  self.payment_method