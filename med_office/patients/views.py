from django.shortcuts import render, redirect
from .forms import PatientForm, HistoryForm
from .models import Patient, History
from django.forms import modelform_factory #útil para crear forms customizables rápidas
# Create your views here.

#This view allows register patients
def mainPatient(request):
    patient = Patient.objects.all()
    patient_form = PatientForm()
    
    if request.method =='POST':
        patient_form = PatientForm(request.POST)
        if patient_form.is_valid():
            patient_form.save()
            patient_form = PatientForm()

    context = {'patient': patient, 'patient_form':patient_form}
    return render(request, 'mainPatient.html', context)
    

def infoPatient(request, id):
    patient = Patient.objects.get(identification=id)
    history = patient.history_set.all()
    context={'patient':patient, 'history':history}

    return render(request,'infoPatient.html', context)

def modifyPatient(request, id):
    patient = Patient.objects.get(identification=id)
    FactoryPatientForm= modelform_factory(Patient, exclude=('identification',))
    patient_form = FactoryPatientForm(instance=patient)
    
    if request.method=='POST':
        patient_form = FactoryPatientForm(request.POST, instance=patient)
        if patient_form.is_valid():
            patient_form.save()
            return redirect('patient')
    
    context= {
        'patient_form':patient_form
    }
    return render(request,'modifyPatient.html', context)


def registerHistory(request):
    history_form = HistoryForm()
    context={'history_form':history_form}

    return render(request,'registerHistory.html', context)

def deletePatient(request, id):
    Patient.objects.filter(identification=id).delete()
    
    return redirect('patient')