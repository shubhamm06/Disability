from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import StudentRegisterForm, StartupRegisterForm, StudentUpdateForm, StartupUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, StudentProfile, StartupProfile


def studentregister(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_student     = True
            user.email          = form.cleaned_data.get('email')
            user.save()
            student             = StudentProfile.objects.create(user=user)
            student.college     = form.cleaned_data.get('college')
            student.contact     = form.cleaned_data.get('contact')
            student.name        = form.cleaned_data.get('name')
            student.cgpa        = form.cleaned_data.get('cgpa')
            student.area_of_specialization  = form.cleaned_data.get('area_of_specialization')
            student.year_of_study           = form.cleaned_data.get('year_of_study')
            student.city_of_residence       = form.cleaned_data.get('city_of_residence')
            student.save()

            messages.success(request, f'Your account has been created! You can login now.')
            return redirect('login')
    else:
        form = StudentRegisterForm()
    return render(request, 'user/signup-student.html', {'form': form})


def startupregister(request):
    if request.method == 'POST' : 
        form = StartupRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.is_startup         = True
            user.email              = form.cleaned_data.get('email')
            user.save()
            startup                 = StartupProfile.objects.create(user=user)
            startup.startup_name    = form.cleaned_data.get('startup_name')
            startup.location        = form.cleaned_data.get('location')
            startup.founders        = form.cleaned_data.get('founders')
            startup.about_the_startup = form.cleaned_data.get('about_the_startup')
            startup.field_of_work   = form.cleaned_data.get('field_of_work')
            startup.website         = form.cleaned_data.get('website')
            startup.startup_logo    = form.cleaned_data.get('startup_logo')
            startup.save()
            messages.success(request, f'Your account has been created successfully!')
            return redirect('login')
    else:
        form = StartupRegisterForm()
    return render(request, 'user/signup-startup.html', {'form': form})


@login_required
def profileupdate(request):
    if request.user.is_student:
        if request.method == 'POST':
            form = StudentUpdateForm(request.POST, request.FILES, instance=request.user.student_profile)

            if form.is_valid():
                form.save()
                messages.success(request, f'Account update successfully!')
                return redirect('profile')

        else:
            form = StudentUpdateForm(instance=request.user.student_profile)
        context = {
            'form': form,
        }

    elif request.user.is_startup:
        if request.method == 'POST':
            form = StartupUpdateForm(request.POST, request.FILES, instance=request.user.startup_profile)

            if form.is_valid():
                form.save()
                messages.success(request, f'Account update successfully!')
                return redirect('profile')

        else:
            form = StartupUpdateForm(instance=request.user.startup_profile)
        context = {
            'form': form,
        }

    else:
        return redirect('home')

    return render(request, 'user/profile-update.html', context)


@login_required   
def profile(request):
    if request.user.is_student:
        context = {
            'object': request.user.student_profile,
        }

        return render(request, 'user/student_profile.html', context)
    
    elif request.user.is_startup:
        context = {
            'object': request.user.startup_profile,
        }

        return render(request, 'user/startup_profile.html', context)

    else:
        return redirect('home')


@login_required
def logout(request):
	return render(request, 'startupEcosystem/ecosystem-home.html')
