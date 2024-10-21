from django.db import models

"""
 Abstract Class have Contact information 
"""
class ContactInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    dob=models.DateField()

    class Meta:
        abstract = True