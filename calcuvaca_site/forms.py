from django import forms

class InsertEmploy(forms.Form):
    name = forms.CharField(label='Nombre del Empleado', max_length=255)
    entry_date = forms.DateField(label='Fecha de Ingreso a la Empresa', widget=forms.DateInput(attrs={'type': 'date'}))

class InsertVacationTaken(forms.Form):
    vacation_days = forms.IntegerField(label="Cantidad de días tomados")
    vacation_date = forms.DateField(label="Fecha de solicitud de vacaciones", widget=forms.DateInput(attrs={'type': 'date'}))
