from django import forms

class contactFrom(forms.Form):
    Temperature = forms.CharField()
    Humidity = forms.CharField()
    pH = forms.CharField()
    Rainfall = forms.CharField()
    
    

