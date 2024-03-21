from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('index',views.index,name='index'),
    path('about',views.about),
    path('contact',views.contact),
    path('register',views.register,name='register'),
    path('coach',views.coach,name='coach'),
    path('coachreg',views.coachreg,name='coachreg'),
    path('coachbook',views.coachbook,name='coachbook'),
    path('coachbooking',views.coachbooking,name='coachbooking'),
    path('coachbooked',views.coachbooked,name='coachbooked'),
    path('mycoachbookings',views.mycoachbookings,name='mycoachbookings'),
    path('cancelcoachbooking',views.cancelcoachbooking,name='cancelcoachbooking'),
    path('deletecoachprofile',views.deletecoachprofile,name='deletecoachprofile'),
    path('login',views.login,name='login'),
    path('coachlogin',views.coachlogin,name='coachlogin'),
    path('coachlogging',views.coachlogging,name='coachlogging'),
    path('registration',views.registration),
    path('coachregistration',views.coachregistration),
    path('logging',views.logging,name='logging'),
    path('main',views.main,name='main'),
    path('viewslot',views.viewslot,name='viewslot'),
    path('bookslot',views.bookslot),
    path('slotbooking',views.slotbooking),
    path('mybookings',views.mybookings,name='mybookings'),
    path('cancelbooking',views.cancelbooking),
    path('dateselect',views.dateselect,name ='dateselect'),
    path('logout',views.loggedout)
]