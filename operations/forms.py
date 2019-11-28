from django import forms
from .models import *

class operationsForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ('nop','libelle','chap','gest',
       'anins','decap','ndins','apinit','apact','sitop','datelanc','consant','consenc','pop',
       'emplp','emplt','physique','taux','prog','dateclot','ndclot','nfixe','numfixe')