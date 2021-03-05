from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from django.db import transaction
from .models import User, StudentProfile, StartupProfile

class StudentRegisterForm(UserCreationForm):
	email 				= forms.EmailField(help_text='Email Id used for registration cannot be changed later.')
	city_of_residence 	= forms.CharField(max_length=40)
	college 			= forms.CharField(max_length=50)
	name 				= forms.CharField(max_length=60)
	contact 			= PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': ('')}), label=("Phone number"), required=False, help_text='Add Country Code before your contact number.') 
	area_of_specialization = forms.CharField(max_length=60, help_text="Enter the course you have currently undertaken at your college.")
	year_of_study		= forms.IntegerField(min_value=1)
	cgpa 				= forms.FloatField(max_value=10, min_value=0, help_text='Enter your CGPA out of 10.')

	class Meta(UserCreationForm.Meta):
		model 	= User
		fields 	= ['name', 'email', 'college', 'area_of_specialization', 'year_of_study', 'cgpa', 'city_of_residence', 'contact', 'password1', 'password2']
	
	@transaction.atomic
	def clean(self):
		email = self.cleaned_data.get('email')

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("Account with this email already exists")
		return self.cleaned_data


class StudentUpdateForm(forms.ModelForm):
	class Meta:
		model = StudentProfile
		fields = ['name', 'college', 'area_of_specialization', 'year_of_study', 'cgpa', 'city_of_residence', 'contact']

class StartupRegisterForm(UserCreationForm):
    startup_name = forms.CharField(max_length=40)
    email = forms.EmailField()
    founders = forms.CharField(max_length=150)
    about_the_startup = forms.CharField(widget=forms.Textarea)
    location = forms.CharField(max_length=40)
    field_of_work = forms.CharField(max_length=50)
    website = forms.URLField(max_length=254)
    startup_logo = forms.ImageField()
	
    class Meta():	
        model = User
        fields = ['startup_name', 'email', 'about_the_startup', 'founders', 'location', 'field_of_work', 'website', 'password1','password2', 'startup_logo',]

    @transaction.atomic
    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Account with this email already exists")
        return self.cleaned_data


class StartupUpdateForm(forms.ModelForm):
	class Meta:
		model = StartupProfile
		fields = ['startup_name', 'about_the_startup', 'founders', 'location', 'field_of_work', 'website', 'startup_logo']