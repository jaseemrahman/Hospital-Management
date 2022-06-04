from django.contrib import admin
from .models import departments,doctor,bookings
# Register your models here.
admin.site.register(departments)
admin.site.register(doctor)
admin.site.register(bookings)