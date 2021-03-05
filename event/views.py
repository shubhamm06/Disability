from django.shortcuts import render

# Create your views here.
def events(request):
    return render(request,'event/events.html')

def esummit(request):
    return render(request,'event/esummit.html')

def vl(request):
    return render(request,'event/vl.html')

def starteco(request):
    return render(request,'event/startupweekend.html')

def etalk(request):
    return render(request,'event/etalks.html')

def etalk2(request):
    return render(request,'event/etalks2.html')

