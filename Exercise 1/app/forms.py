from django import forms

class HelloForm(forms.Form):
    name = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class AgeForm(forms.Form):
    end = forms.IntegerField()
    birth = forms.IntegerField()
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class OrderForm(forms.Form):
    burger = forms.IntegerField()
    fries = forms.IntegerField()
    drink = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data