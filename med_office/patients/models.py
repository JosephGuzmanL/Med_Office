from django.db import models
# Create your models here.

class Patient(models.Model):
    blood_type_choices=[
        (1,'A+'),(2,'A-'),
        (3,'B+'),(4,'B-'),
        (5,'AB+'),(6,'AB-'),
        (7,'O+'),(8,'O-'),
    ]
    status_choices = [
        (1, 'SINGLE'),
        (2,'MARRIED'),
    ]
    identification = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    blood_type = models.SmallIntegerField(choices=blood_type_choices)
    status = models.SmallIntegerField(choices=status_choices)
