from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'home.html')


def main(request):
    return render(request,'choose.html')

def bmi(request):
    return render(request,'bmi.html')
