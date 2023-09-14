from django.shortcuts import render

from .models import Project

# Create your views here.

def project_index(request):

    context = {
        "projects": Project.objects.all()
    }
    return render(request, "project_index.html", context)


def project_detail(request, id):

    context = {
        "project": Project.objects.get(pk=id)
    }
    return render(request, "project_detail.html", context)