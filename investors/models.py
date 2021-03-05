from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Investor(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=200)
    startups_funded = models.CharField(max_length=500, default='')
    contact = PhoneNumberField(blank=True, null=True, help_text='Add country code before the contact no.')
    email = models.EmailField(default='')
    photo = models.ImageField(default='', upload_to='vc/')

    
    def __str__(self):
        return self.name