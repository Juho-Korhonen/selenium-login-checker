from django.shortcuts import render
from .models import About_me,Project
# Create your views here.


def display_about_me_page(request):
    about_me = About_me.objects.get(id=1)
    return render(request,'sites/about_me.html',{'models':about_me})


def display_contact_page(request):
    return render(request,'sites/contact.html')

def display_project_page(request):
    projects = Project.objects.all()
    return render(request,'sites/projects.html',{'projects':projects})