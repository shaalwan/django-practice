from django.shortcuts import render
from .models import Project


def project(requests):
    projects = Project.objects.all()
    return render(requests, 'portfolio/home.html',{'projects':projects})

