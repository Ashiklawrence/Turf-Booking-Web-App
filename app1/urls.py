from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('index',views.index,name='index'),
    path('about',views.about),
    path('contact',views.contact),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('registration',views.registration),
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