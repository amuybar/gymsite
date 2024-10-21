from django.contrib import admin

from classes.models import ClassSchedule, Booking, Attendance

admin.site.register(ClassSchedule)
admin.site.register(Booking)
admin.site.register(Attendance)
