from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    data=course.objects.all()
    # print(data)
    return render(request, 'home.html',{'data':data})
def gift(request):
    return render(request, 'gift.html')
def profile(request):
    return render(request, 'profile.html')
def learn(request):
    return render(request, 'learn.html')
def pro(request):
    form = prosForm(request.POST)
    if form.is_valid():
        form.save()
    p1=prosForm()
    return render(request,'pro.html',{'form':p1})
def setting(request):
    return render(request, 'setting.html')
def courses(request):
    data=course.objects.all()
    # print(data)
    return render(request, 'courses.html',{'data':data})
def find(request):
    return render(request,'find.html')