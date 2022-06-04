# from dataclasses import fields
from django import forms
from .models import bookings

class Dateinput(forms.DateInput):
    input_type='Date'

class bookingform(forms.ModelForm):
    class Meta:
        model=bookings
        fields='__all__'
        widgets={
            'booking_date':Dateinput(),
        }
        labels={
            'p_name':'Patient Name: ',
            'p_phone':'Patient Phone: ',
            'p_email':'Patient Email: ',
            'dep_name':'Department Name: ',
            'doc_name':'Doctor Name: ',
            'Booking_date':'Booking Date: ',
        }