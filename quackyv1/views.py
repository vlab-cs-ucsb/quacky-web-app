from django.shortcuts import render
from .forms import *

def aws(request):
    form = AWSForm()
    return render(request, 'aws.html', {'form': form})

def azure(request):
    form = AzureForm()
    return render(request, 'azure.html', {'form': form})

def gcp(request):
    form = GCPForm()
    return render(request, 'gcp.html', {'form': form})
