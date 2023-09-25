from django.shortcuts import render,redirect
from .forms import RefugeeForm
from .models import Refugee
from django.views.generic import CreateView
from .logic import receive_data
# Create your views here.

def time_page(request):
    return render(request, 'time.html')

def thank_you(request):
    return render(request, 'thank_you.html',)

def index(request):
    refugee = RefugeeForm()
    if request.method == "POST":
        refugee = RefugeeForm(request.POST)
        if refugee.is_valid():
            refugee.save()
            current_refugee = refugee.cleaned_data
            service1 = str(refugee.cleaned_data.get('service'))
            service2 = str(refugee.cleaned_data.get('service2'))
            reg_services = ["Verification/Document Renewal", "New Registration", "Family Add-on", "Family Unity Interview",
                        "Closure", "Contact Update"]
            rsd_services = ["RSD : Interview", "RSD : Result"]
            subjects = ("RST", rsd_services, "Health", "Protection", "CBI", "Residency", reg_services)
            sending_subjects = ("RST", "RSD", "Health", "Protection", "CBI", "Residency", "Registration")
            
            i = 0
            while i < 7:
                for subject in subjects:
                    if service1 in subjects[i]: 
                        receive_data(current_refugee=current_refugee, subject_received=sending_subjects[i])
                    if service2 in subjects[i]: 
                        receive_data(current_refugee=current_refugee, subject_received=sending_subjects[i])
                    i += 1
                        
            return redirect('thank_you')
    return render(request, 'index.html',{'form':refugee})
