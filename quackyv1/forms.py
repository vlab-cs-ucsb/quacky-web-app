from django import forms

class AWSForm(forms.Form):
    policy1 = forms.CharField(required = False, widget = forms.Textarea(attrs = {
        'id': 'policy1'
    }))
    policy2 = forms.CharField(required = False, widget = forms.Textarea(attrs = {
        'id': 'policy2'
    }))
    bound = forms.IntegerField(required = True, initial = 100, widget = forms.NumberInput(attrs = {
        'class': 'form-control',
        'placeholder': '100'
    }))
    constraints = forms.BooleanField(required = False, widget = forms.CheckboxInput(attrs = {
        'class': 'form-check-input'
    }))
    encoding = forms.BooleanField(required = False, widget = forms.CheckboxInput(attrs = {
        'class': 'form-check-input'
    }))

class AzureForm(forms.Form):
    role_definitions = forms.CharField(required = False, widget = forms.Textarea(attrs = {
        'id': 'roledefinitions'
    }))
    role_assignment1 = forms.CharField(required = False, widget = forms.Textarea(attrs = {
        'id': 'roleassignment1'
    }))
    role_assignment2 = forms.CharField(required = False, widget = forms.Textarea(attrs = {
        'id': 'roleassignment2'
    }))
    bound = forms.IntegerField(required = True, initial = 150, widget = forms.NumberInput(attrs = {
        'class': 'form-control',
        'placeholder': '150'
    }))
    constraints = forms.BooleanField(required = False, widget = forms.CheckboxInput(attrs = {
        'class': 'form-check-input'
    }))
    encoding = forms.BooleanField(required = False, widget = forms.CheckboxInput(attrs = {
        'class': 'form-check-input'
    }))

class GCPForm(forms.Form):
    role = forms.CharField(required = False, widget = forms.Textarea(attrs = {
        'id': 'role'
    }))
    role_bindings1 = forms.CharField(required = False, widget = forms.Textarea(attrs = {
        'id': 'rolebindings1'
    }))
    role_bindings2 = forms.CharField(required = False, widget = forms.Textarea(attrs = {
        'id': 'rolebindings2'
    }))
    bound = forms.IntegerField(required = True, initial = 150, widget = forms.NumberInput(attrs = {
        'class': 'form-control',
        'placeholder': '150'
    }))
    constraints = forms.BooleanField(required = False, widget = forms.CheckboxInput(attrs = {
        'class': 'form-check-input'
    }))
    encoding = forms.BooleanField(required = False, widget = forms.CheckboxInput(attrs = {
        'class': 'form-check-input'
    }))