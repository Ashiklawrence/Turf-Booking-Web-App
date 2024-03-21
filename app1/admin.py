from django.contrib import admin
from app1.models import Slot,BookedSlot,UserInfo,CoachInfos,BookedCoach
# Register your models here.




class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Phno','username','password')

admin.site.register(UserInfo,UserInfoAdmin)

class CoachInfosAdmin(admin.ModelAdmin):
    list_display = ('Image','Name','Sports','Summary','Charge','username','password')

admin.site.register(CoachInfos,CoachInfosAdmin)

class BookedCoachAdmin(admin.ModelAdmin):
    list_display = ('Coach','Sports','Bookdate','Time','Bookeddate','Bookedby')

admin.site.register(BookedCoach,BookedCoachAdmin)

class SlotAdmin(admin.ModelAdmin):
    list_display = ('Slotname','Timerange')

admin.site.register(Slot,SlotAdmin)

class BookedSlotAdmin(admin.ModelAdmin):
    list_display = ('Bookingid','Slotname','Timerange','Bookedby','Bookeddate','Slotdate')

admin.site.register(BookedSlot,BookedSlotAdmin)