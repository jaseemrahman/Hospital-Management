# from ast import Return
# from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

from .forms import bookingform

from .models import departments,doctor,bookings
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def booking(request):
    if request.method=='POST':
        form=bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')

    form=bookingform()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)
def doctors(request):
    dict_doc={ 
        'doctors':doctor.objects.all()
    }
    return render(request,'doctors.html',dict_doc)
def department(request):
    dict_dept={
        'dept':departments.objects.all()
    }
    return render(request,'department.html',dict_dept)
def contact(request):
    return render(request,'contact.html') 