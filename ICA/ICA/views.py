from django.http import HttpResponse
from django.shortcuts import render

def home(request) :
	return render(request,'home.html')

def success(request) :
	return render(request, 'success.html')

def profile(request) :
	return render(request, 'profile.html')