from django.shortcuts import render, redirect
from .forms import PatientForm
from .models import Patient

# Create your views here.
def mainPatient(request):
    patient = Patient.objects.all()
    context = {'patient':patient}
    return render(request,'mainPatient.html', context)

def registerPatient(request):
    if request.method=='POST':
        patient_form = PatientForm(request.POST)
        if patient_form.is_valid():
            patient_form.save()
            return redirect('patient')
    else:
        patient_form = PatientForm()
    context = {'patient_form':patient_form}
    return render(request, 'registerPatient.html', context)

def infoPatient(request, id):
    patient = Patient.objects.get(identification=id)
    context={'patient':patient}
    return render(request,'infoPatient.html', context)

def modifyPatient(request, id):
    patient = Patient.objects.get(identification=id)
    patient_form = PatientForm(instance=patient)
    
    if request.method=='POST':
        patient_form = PatientForm(request.POST, instance=patient)
        if patient_form.is_valid():
            patient_form.save()
            return redirect('patient')
    
    context= {
        'patient_form':patient_form
    }
    return render(request,'modifyPatient.html', context)