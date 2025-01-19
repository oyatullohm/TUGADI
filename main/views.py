from django.views.generic import DetailView
from .models import Certificate
from django.shortcuts import render
class CertificateDetailView(DetailView):
    model = Certificate
    template_name = 'index.html' 
    context_object_name = 'certificate'


def Index(request):
    context={
        'certificate':Certificate.objects.first()

    }
    return render(request,'about.html',context)