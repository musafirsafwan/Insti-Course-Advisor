from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from registration_stud.forms import UserCreateForm

def register_stud(request) :
	if request.method == 'POST' :
		form = UserCreateForm(request.POST)
		if form.is_valid() :
			new_user = form.save()
			return HttpResponseRedirect("/success/")
	else :
		form = UserCreateForm()
	return render(request,"registration/stud.html", {
		'form' : form,
	})