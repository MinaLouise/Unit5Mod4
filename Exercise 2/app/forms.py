from django import forms


class FrontForms(forms.Form):
    word = forms.CharField()
    n = forms.IntegerField()

class TeenSumForms(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()

class ThereForms(forms.Form):
    s = forms.CharField()

class CenteredForms(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()
    d = forms.IntegerField()
    e = forms.IntegerField()
    f = forms.IntegerField(required=False)
    g = forms.IntegerField(required=False)