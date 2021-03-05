from django import forms
from .models import Post
from django.http import request

class PostCreateForm(forms.ModelForm):	
	class Meta():
		model 	= Post
		fields=['title','content','blog_image','author','about_the_author','author_image','email']

class PostUpdateForm(forms.ModelForm):	
	class Meta():
		model 	= Post
		fields=['title','content','blog_image','date_published','author','about_the_author','author_image','email','is_published']
