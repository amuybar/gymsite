from django.contrib import admin

from members.models import Member, MemberShipType

admin.site.register(Member)
admin.site.register(MemberShipType)
