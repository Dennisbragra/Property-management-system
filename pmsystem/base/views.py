from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import House, Topic
from .forms import NewUnit, SoldUnit


# Create your views here.

def home(request):
	topics = Topic.objects.all()
	
	houses = House.objects.all()
	
	units = House.objects.filter(sold=False)[0:1]

	context = {'topics':topics, 'houses':houses, 'units':units}

	return render(request, 'index.html', context)

def catalogue(request, pk):
	topic = Topic.objects.get(id=pk)
	houses = topic.house_set.all()

	context = {'topic':topic, 'houses':houses}		
	return render(request, 'catalogue.html', context)

def view_unit(request, pk):
	house = House.objects.get(id=pk)
	
	context = {'house':house}
	return render(request, 'view_unit.html', context)


def book_unit(request, pk):
	house = House.objects.get(id=pk)

	form = SoldUnit(instance=house)

	if request.method == 'POST':
		form = SoldUnit(request.POST, instance=house)
		if form.is_valid():
			form.save()
			return redirect('home')


	context = {'form':form, 'house':house}		
	return render(request, 'book_unit.html', context)

def newUnit(request):
	form = NewUnit()

	if request.method == 'POST':
		form = NewUnit(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'form':form}
	return render(request, 'new_unit.html', context)

def registerPage(request):
	form = UserCreationForm()
	
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			tenant = form.save(commit=False)
			tenant.username = tenant.username.lower()
			tenant.save()
			login(request, tenant)
			return redirect('home')
		else:
			messages.error(request, 'Something Happened')	
	context = {'form':form}
	return render(request, 'login_register.html', context)

def loginPage(request):
	page = 'login'
	if request.method == 'POST':
		username = request.POST.get('username').lower()
		password = request.POST.get('password')

		try:
			user = User.objects.get(username=username)
		except:
			messages.error(request, 'User does not exist')	

		tenant = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')	
		else:
			messages.error(request, 'Username or password does not exist')	

	context = {'page':page}
	return render(request, 'login_register.html', context)

def logoutPage(request):
	logout(request)
	return redirect('home')






def about(request):
	return render(request, 'about.html')

def house_status(request):
	sold_units = House.objects.filter(sold=True)
	booked_units = House.objects.filter(booked=True)


	context = {'sold_units':sold_units, 'booked_units':booked_units}
	return render(request, 'house_status.html', context)

def mybooked_units(request):
	
	units = House.objects.filter(booked=True)

	
	context = {'units':units}
	return render(request, 'my_units.html', context)				