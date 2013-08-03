from django import forms

class EmailForm(forms.form):
    email = forms.CharField(max_length=128)
