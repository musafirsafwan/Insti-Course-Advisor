from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
	firstname = forms.CharField()
	lastname = forms.CharField()
	rollnumber = forms.CharField()
	hostel = forms.CharField()
	phonenumber = forms.CharField()
	email = forms.EmailField()

	class Meta :
		model = User
		fields = ("firstname","lastname","username","rollnumber","hostel","phonenumber","email","password1","password2")

	def save(self, commit=True) :
		user = super(UserCreateForm,self).save(commit=False)
		user.firstname = self.cleaned_data["firstname"]
		user.lastname = self.cleaned_data["lastname"]
		user.rollnumber = self.cleaned_data["rollnumber"]
		user.hostel = self.cleaned_data["hostel"]
		user.phonenumber = self.cleaned_data["phonenumber"]
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user