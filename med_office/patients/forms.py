from django import forms
from .models import Patient, History

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        exclude = ['date_of_creation', 'diagnostic', 'recomendation','recomendate_medicine']
        widgets = {
            'date_of_consult':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control','place-holder':'Select a date', 'type':'date'}),
        }