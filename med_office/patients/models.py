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

    def __str__(self):
        return (self.name + self.last_name)

class History(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    companion = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    height = models.DecimalField(max_digits=3, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    reason = models.TextField()
    diagnostic = models.TextField()
    recomendation = models.TextField(blank=True)
    recomendate_medicine = models.TextField(blank = True)