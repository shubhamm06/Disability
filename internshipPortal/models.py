from django.db import models
from django.urls import reverse
from user.models import StartupProfile, StudentProfile
from markdown_deux import markdown
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField

class Internship(models.Model):
    startup = models.ForeignKey(StartupProfile, on_delete=models.CASCADE, related_name='internships_created', default='')
    field_of_internship = models.CharField(max_length=100, default='')
    duration = models.CharField(max_length=20)
    about = models.TextField()
    location = models.CharField(max_length=100)
    stipend = models.CharField(max_length=100)
    skills_required = models.CharField(max_length=500)
    no_of_internships = models.PositiveIntegerField()
    perks = models.CharField(max_length=100)
    apply_by = models.DateField(default='2000-01-01', help_text='YYYY-MM-DD Format should be followed for the date.')

    who_should_apply = models.CharField(max_length=200)

    def __str__(self):
        return self.startup.startup_name + "(" + str(self.id) + ")"

    def get_absolute_url(self):
        return reverse('internship-detail', kwargs={'pk' : self.pk})

    def about_markdown(self):
        about = self.about
        return mark_safe(markdown(about))

    def get_next_post(self):
        next_post = self.get_previous_by_apply_by()
        if next_post:
        	return next_post
        return False   	

    def get_prev_post(self):
        prev_post = self.get_next_by_apply_by()
        if prev_post:
        	return prev_post
        return False

class InternshipApplication(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE, default='', related_name='internship')
    message = models.TextField(max_length = 1200, blank=True, default='')
    resume = models.URLField(default='', help_text='Add the drive link to your resume.')
    applied_by = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, default='', related_name='intern')
    
    def __str__(self):
        return self.internship.startup.startup_name + "(" + str(self.internship.id) + ")" + " - " + self.applied_by.name

    def message_markdown(self):
        message = self.message
        return mark_safe(markdown(message))

class VentureCapitalist(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=550)
    startups_funded = models.CharField(max_length=500, default='')
    contact = PhoneNumberField(blank=True, null=True, help_text='Add country code before the contact no.')
    email = models.EmailField(default='')
    photo = models.ImageField(default='', upload_to='vc/')
    industries = models.CharField(max_length=500, default='')


    def __str__(self):
        return self.name
