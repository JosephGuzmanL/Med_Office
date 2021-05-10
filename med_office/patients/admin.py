from django.contrib import admin
from .models import Patient, History, Medicine
# Register your models here.
admin.site.register(Patient)
admin.site.register(History)
admin.site.register(Medicine)