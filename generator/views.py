from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request,'generator/home.html')


def password(request):
    thepassword=""
    chars=list('zxcvbnmasdfghjrwru')
    if request.GET.get('upercase'):
        chars.extend(list('ASDFGHJKLMNBVCXZQWERTTYYUIO'))
    if request.GET.get('number'):
        chars.extend(list('1234567890'))
    if request.GET.get('special'):
        chars.extend(list('!@#$%^&*()_+'))
    length=int(request.GET.get('length',14))
    
    
    for x in range(length):
        thepassword+=random.choice(chars)
    return render(request,'generator/password.html',{'password':thepassword})


def aboutus(request):
    return render(request,'generator/aboutus.html',{"strshow":"Hello"})

