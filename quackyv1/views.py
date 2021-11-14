from django.shortcuts import render

def aws(request):
    return render(request, 'aws.html')

def azure(request):
    return render(request, 'azure.html')

def gcp(request):
    return render(request, 'gcp.html')
