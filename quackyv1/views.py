from django.shortcuts import render
from .forms import *
from .utils import *

# AWS analysis view
def aws(request):
    # POST request
    if request.method == 'POST':
        form = AWSForm(request.POST)
        
        # form valid
        if form.is_valid():
            d = form.cleaned_data
            
            # Note: the emptiness check on the textareas is being done here
            # because CodeMirror would not cooperate if I set required=True
            # in forms.py

            # dispatch to handler function
            if not d['policy1'] or d['policy1'].isspace():
                results = FAILURE
            elif d['policy2'] and not d['policy2'].isspace():
                results = ta_aws_multi(d)
            else:
                results = ta_aws_single(d)
            
            # render filled form and results
            return render(request, 'aws.html', {
                'form': form, 
                'results': results
            })

        # form invalid; render filled form but not results
        else:
            return render(request, 'aws.html', {'form': form})

    # GET request; render fresh form
    else:
        form = AWSForm()
        return render(request, 'aws.html', {'form': form})

# Azure analysis view
def azure(request):
    if request.method == 'POST':
        form = AzureForm(request.POST)
        
        if form.is_valid():
            d = form.cleaned_data

            if not d['role_definitions'] or not d['role_assignment1']:
                results = FAILURE
            elif d['role_definitions'].isspace() or d['role_assignment1'].isspace():
                results = FAILURE
            elif d['role_assignment2'] and not d['role_assignment2'].isspace():
                results = ta_azure_multi(d)
            else:
                results = ta_azure_single(d)

            return render(request, 'azure.html', {
                'form': form, 
                'results': results
            })

        else:   
            return render(request, 'azure.html', {'form': form})

    else:
        form = AzureForm()
        return render(request, 'azure.html', {'form': form})

# GCP analysis view
def gcp(request):
    if request.method == 'POST':
        form = GCPForm(request.POST)
        
        if form.is_valid():
            d = form.cleaned_data

            if not d['role'] or not d['role_bindings1']:
                results = FAILURE
            elif d['role'].isspace() or d['role_bindings1'].isspace():
                results = FAILURE
            elif d['role_bindings2'] and not d['role_bindings2'].isspace():
                results = ta_gcp_multi(d)
            else:
                results = ta_gcp_single(d)

            return render(request, 'gcp.html', {
                'form': form, 
                'results': results
            })

        else:   
            return render(request, 'gcp.html', {'form': form})

    else:
        form = GCPForm()
        return render(request, 'gcp.html', {'form': form})

def usage(request):
    return render(request, 'usage.html')