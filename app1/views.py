from django.shortcuts import render,redirect
from app1.models import Slot,BookedSlot,UserInfo
from django.contrib.auth import authenticate,login as authlogin,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
# from django.http import response

# Create your views here.
def index(request):
    return render(request,'index.html')
        



def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

@login_required(login_url='login')
def bookslot(request):
    return render(request,'bookslot.html')



def registration(request):
    a = request.POST['name']
    b = request.POST['email']
    c = request.POST['phno']
    d = request.POST['username']
    e = request.POST['password']
    f = request.POST['cnfrmpassword']
    if UserInfo.objects.filter(username = d).exists():
        exist = True
        return render(request,'register.html',{'exist_msg':exist})
    elif e == f:
        x = UserInfo.objects.create_user(Name = a, Email = b, Phno = c, username = d, password = e)
        x.save()
        success = True
        return render(request,'register.html',{'success_msg':success})
    else:
        error = True
        # messages.error(request,'Password does not match')
        return render(request,'register.html',{'error_msg':error})

def logging(request):
    if request.POST:
        u = request.POST['username']
        p = request.POST['password']
        try:
            x = UserInfo.objects.get(username = u)
            user = authenticate(username=u,password=p)
            if user:
                authlogin(request,user)
                # return render(request,'main.html',{'key':x})
                return redirect('main')
            else:
                error = True
                return render(request,'login.html',{'error_msg':error})
        except:
            exist = True
            return render(request,'login.html',{'exist_msg':exist})

@login_required(login_url='login')
def main(request):
    a = request.user
    x = UserInfo.objects.get(username = a)
    return render(request,'main.html',{'key':x})
        
@login_required(login_url='login')  
def viewslot(request):
    x = Slot.objects.all()
    y = BookedSlot.objects.all()
    return render(request,'viewslot.html',{'slots':x,'bookedslots':y})


@login_required(login_url='login')
def dateselect(request):
    a = request.POST['slotdate']
    e = BookedSlot.objects.filter(Slotdate=a)
    f = e.values_list('Slotname',flat = True)
    x = Slot.objects.all()
    return render(request,'viewslot.html',{'slots':x,'date':a,'booked':f})

@login_required(login_url='login')
def slotbooking(request):
    a = request.POST['idnum']
    b = request.POST['slotname']
    c = request.POST['timerange']
    # d = request.COOKIES.get('cur_user')
    d = request.user
    e = request.POST['bookeddate']
    f = request.POST['slotdate']
    s = BookedSlot(Bookingid = a,Slotname = b,Timerange = c,Bookedby =d,Bookeddate=e,Slotdate=f)
    s.save()
    success = True
    x = Slot.objects.all()
    # slot list
    g = BookedSlot.objects.filter(Slotdate=f)
    h = g.values_list('Slotname',flat = True)
    return render(request,'viewslot.html',{'slots':x,'msg':success,'slot_name':b,'date':f,'booked':h})
    # messages.success('Slot Booked succesfully')
    # return redirect('viewslot')

@login_required(login_url='login')
def mybookings(request):
    # a = request.COOKIES.get('cur_user')
    a = request.user
    x = BookedSlot.objects.filter(Bookedby=a)
    ex = BookedSlot.objects.filter(Bookedby=a).exists()
    return render(request,'mybookings.html',{'key':x,'exist':ex})

    
@login_required(login_url='login')
def cancelbooking(request):
    a = request.POST['idnum']
    # b = request.COOKIES.get('cur_user')
    b = request.user
    c = request.POST['slotname']
    BookedSlot.objects.filter(id=a).delete()
    cancel = True
    x = BookedSlot.objects.filter(Bookedby=b)
    ex = BookedSlot.objects.filter(Bookedby=b).exists()
    # return redirect('mybookings')
    return render(request,'mybookings.html',{'key':x,'msg':cancel,'slot_name':c,'exist':ex})


@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required(login_url='login')
def loggedout(request):
    logout(request)
    return redirect('index')










