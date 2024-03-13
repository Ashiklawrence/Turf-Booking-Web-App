from django.contrib import admin
from app1.models import UserDetail,Slot,BookedSlot,UserInfo
# Register your models here.




class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Phno','username','password')

admin.site.register(UserInfo,UserInfoAdmin)



class SlotAdmin(admin.ModelAdmin):
    list_display = ('Slotname','Timerange')

admin.site.register(Slot,SlotAdmin)

class BookedSlotAdmin(admin.ModelAdmin):
    list_display = ('Bookingid','Slotname','Timerange','Bookedby','Bookeddate','Slotdate')

admin.site.register(BookedSlot,BookedSlotAdmin)