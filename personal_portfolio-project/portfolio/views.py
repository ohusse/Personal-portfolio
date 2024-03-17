from django.shortcuts import render
from .models import Project
from certifications.models import Certification

def home(request):
    certifications = Certification.objects.all()[:3]
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects, 'certifications':certifications})
    