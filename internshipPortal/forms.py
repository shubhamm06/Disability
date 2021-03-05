from django import forms
from .models import Internship, InternshipApplication, VentureCapitalist


class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = [
            'field_of_internship',
            'duration',
            'about',
            'location',
            'stipend',
            'skills_required',
            'no_of_internships',
            'perks',
            'who_should_apply',
            'apply_by',
        ]


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = InternshipApplication
        fields = [
            'message',
            'resume',
        ]


class VenCapForm(forms.ModelForm):
    class Meta:
        model = VentureCapitalist
        fields = [
            'name',
            'about',
            'startups_funded',
            'contact',
            'email',
            'photo',
            'industries',
        ]    
