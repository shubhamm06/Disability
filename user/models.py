from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password=None):
        user = self.model(email=email, is_staff=True, is_superuser=True)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Email Address', unique=True)
    is_student = models.BooleanField(default=False)
    is_startup = models.BooleanField(default=False)
    is_team = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name ='student_profile')
    name = models.CharField(max_length=60, default='')
    city_of_residence = models.CharField(max_length=40, default='')
    college = models.CharField(max_length=50, default='')
    area_of_specialization = models.CharField(max_length=60, default='')
    year_of_study = models.IntegerField(default=1)
    contact = PhoneNumberField(blank=False)
    cgpa = models.FloatField(default=0)

    def __str__(self):
        return self.user.email


class StartupProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name = 'startup_profile')
    startup_name = models.CharField(max_length=40, default='')
    about_the_startup = models.TextField(max_length=500, blank=True)
    founders = models.CharField(max_length=150, default='')
    location = models.CharField(max_length=100, default='')
    field_of_work = models.CharField(max_length=50)
    website = models.URLField(default='', null=True, blank=True)
    startup_logo = models.ImageField(default='startup/download.png', upload_to='startup/')
    to_publish = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email
