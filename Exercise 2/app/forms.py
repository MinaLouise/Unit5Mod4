from django import forms


class FrontForms(forms.Form):
    word = forms.CharField()
    n = forms.IntegerField()