from django.shortcuts import render
from .models import Certification

def all_certifications(request):
    certifications = Certification.objects.order_by('-date')
    return render(request, 'certifications/all_certifications.html', {'certifications':certifications})

