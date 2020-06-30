from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils.http import is_safe_url
import re
from .forms import SignUpForm
from datetime import date, datetime, timedelta
#import datetime as d

from .models import Apartment, Booking, Category, Bedtype, Guestnum

# Create your views here.
def index(request):
    return render(request, 'hotel/index.html')

def apartments(request):
    context = {
        "apartments": Apartment.objects.all(),
    }
    return render(request, 'hotel/apartments.html', context)

def apartment(request, apartment_id):
    apartment = Apartment.objects.get(pk=apartment_id)
    x = Booking.objects.filter(apartment__pk=apartment_id).values('check_in', 'check_out')
    y = [entry for entry in x]
    bookings = []
    for i in y:
        num_days = (i["check_out"] - i["check_in"]).days
        bookings.append(i["check_in"].isoformat())
        bookings.append(num_days)


    context = {
        'apartment': apartment,
        'bookings': bookings,
    }
    return render(request, 'hotel/apartment.html', context)

def book(request):
    check_in = request.POST.get('check-in')
    check_out = request.POST.get('check-out')
    check_id = request.POST.get('check-id')
    cot_bed = request.POST.get('cot')
    cot = False
    if not cot_bed:
        cot = False
    else:
        cot = True

    day_in = datetime.strptime(check_in, '%Y-%m-%d').date()
    day_out = datetime.strptime(check_out, '%Y-%m-%d').date()
    days = (day_out - day_in).days
    dates = []
    for x in range(days):
        date_split = str(day_in).split('-')
        last = ''
        if date_split[2][0] == 0:
            last = '0' + (int(date_split[2]) + x)
        else:
            last = int(date_split[2]) + x
        date_split[2] = str(last)
        new_date = '-'.join(date_split)
        dates.append(new_date)
    
    x = Booking.objects.filter(apartment__pk=check_id).values('check_in', 'check_out')
    y = [entry for entry in x]
    booked_dates = []
    for i in y:
        booked_day_in = i["check_in"] 
        booked_day_out = i["check_out"] 
        booked_days = (booked_day_out - booked_day_in).days
        for x in range(booked_days):
            date_split = str(booked_day_in).split('-')
            last = int(date_split[2]) + x
            date_split[2] = str(last)
            new_date = '-'.join(date_split)
            booked_dates.append(new_date)
    
    #get total cost
    a = Apartment.objects.get(pk=check_id)
    apartment = Apartment.objects.filter(pk=check_id).values('cost_per_night')
    apartment_cost = [entry for entry in apartment]
    cost = 0
    for i in apartment_cost:
        cost = i['cost_per_night']
    total_cost = cost * days

    date_conflict = set(dates) & set(booked_dates)
    if date_conflict:
        raise Http404('The dates are not available. Please choose other dates.')
    else:
        booked = Booking(apartment=a, user_id=request.user.id, check_in=check_in, check_out=check_out, extra_bed=cot, total_cost=total_cost)
        booked.save()
        return redirect('bookings')

def search(request):
    check_in = request.POST.get('search-check-in')
    check_out = request.POST.get('search-check-out')

    #dates requested
    day_in = datetime.strptime(check_in, '%Y-%m-%d').date()
    day_out = datetime.strptime(check_out, '%Y-%m-%d').date()
    days = (day_out - day_in).days
    dates = []
    for x in range(days):
        date_split = str(day_in).split('-')
        last = ''
        if date_split[2][0] == 0:
            last = '0' + (int(date_split[2]) + x)
        else:
            last = int(date_split[2]) + x
        date_split[2] = str(last)
        new_date = '-'.join(date_split)
        dates.append(new_date)

    #booked dates
    x = Booking.objects.all().values('apartment_id', 'check_in', 'check_out')
    print(f"booked apts: {x}")
    y = [entry for entry in x]
    not_available = []
    for i in y:
        booked_dates = []
        print(f"booked: {i}")
        booked_day_in = i["check_in"] 
        booked_day_out = i["check_out"]
        booked_apt = i["apartment_id"]
        booked_days = (booked_day_out - booked_day_in).days
        for x in range(booked_days):
            date_split = str(booked_day_in).split('-')
            last = int(date_split[2]) + x
            date_split[2] = str(last)
            new_date = '-'.join(date_split)
            booked_dates.append(new_date)
        date_conflict = set(dates) & set(booked_dates)
        if date_conflict:
            not_available.append(booked_apt)
    print(f"not_available: {not_available}")

    context = {
        'apartments': Apartment.objects.all(),
        'not_available': not_available,
        'check_in': check_in,
        'check_out': day_out,
        'days': days,

    }
    return render(request, 'hotel/searchresults.html', context)

def bookings(request):
    existing_bookings = Booking.objects.filter(user_id=request.user.id)
    context = {
        'bookings': existing_bookings,
    }
    return render(request, 'hotel/bookings.html', context)

def about(request):
    return render(request, 'hotel/about.html')


def login_view(request):
    redirect_to = request.POST.get('next')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(redirect_to)
    else:
        return render(request, "hotel/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "hotel/index.html", {"message": "Logged out."})

def register(request):
    redirect_to = request.POST.get('next')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You Have Been Registered'))
            return redirect(redirect_to)
    else:
        form = SignUpForm()
    
    context = {'form': form}
    return render(request, 'hotel/register.html', context)