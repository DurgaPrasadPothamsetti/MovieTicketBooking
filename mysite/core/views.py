from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Tickets, AddPrice, AddMovie
import pyqrcode
import png

@login_required
def homee(request):
    return render(request, 'base.html')
def bookings(request):
    booking_view =request.POST.get('booking_view')
    tickets = Tickets.objects.filter(user_name=booking_view)
    context = {'tickets': tickets}
    return render(request, 'history.html',context=context)
def ticket(request):
    tickets = Tickets.objects.all().order_by('-id')[:1]
    
    context = {'tickets': tickets}
    return render(request, 'ticket.html',context=context)
def home(request):
    details = AddMovie.objects.all()
    context = {'details': details}
    return render(request, 'home.html', context=context)
def booking(request):
   
    return render(request, 'booking.html')
def confirm(request):
    print("hello form is submitted")
   # user_name = request.POST['user_name']
    user_name=request.POST.get('user_name')
    seat_count = request.POST.get('seat_count')
    seat_numbers = request.POST.get('seat_numbers')
    total_amount = request.POST.get('total_amount')
    
    tickets = Tickets(user_name=user_name,seat_count=seat_count,seat_numbers=seat_numbers,total_amount=total_amount)
    
    tickets.save()
    tickets = Tickets.objects.filter(user_name=user_name).order_by('-id')[:1]
    context = {'tickets': tickets}
    return render(request, 'diss.html',context=context)
    


def signup(request):
    if request.method == 'POST':
        
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
