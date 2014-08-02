from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from registration_prof.forms import UserCreateForm

def register_prof(request) :
	if request.method == 'POST' :
		form = UserCreateForm(request.POST)
		if form.is_valid() :
			new_user = form.save()
			return HttpResponseRedirect("/success/")
	else :
		form = UserCreateForm()
	return render(request,"registration/prof.html", {
		'form' : form,
	})