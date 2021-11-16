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
    role_definition = forms.CharField(required = False, widget = forms.Textarea(attrs = {
        'id': 'roledefinition'
    }))
    role_assignments = forms.CharField(required = False, widget = forms.Textarea(attrs = {
        'id': 'roleassignments'
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
    role_bindings = forms.CharField(required = False, widget = forms.Textarea(attrs = {
        'id': 'rolebindings'
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