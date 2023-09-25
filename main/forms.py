from django import forms
from .models import Refugee


class RefugeeForm(forms.ModelForm):
    class Meta:
        model = Refugee
        fields = ('name', 'file_no', 'phone_number', 'nationality', 'service', 'service2', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameinput'}),
            'file_no': forms.TextInput(attrs={'class': 'form-control', 'id': 'fileinput'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'id': 'phoneinput'}),
            'nationality': forms.Select(attrs={'class': 'form-control', 'id': 'natinput'}),
            'service': forms.Select(attrs={'class': 'form-control', 'id': 'serviceinput'}),
            'service2': forms.Select(attrs={'class': 'form-control', 'id': 'service2input'}),
            'message': forms.Textarea(attrs={'class': 'textarea', 'rows': 7}),
        }
