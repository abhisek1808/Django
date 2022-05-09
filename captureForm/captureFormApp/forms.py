from django import forms

class studentform(forms.Form):
    sname=forms.CharField(max_length=30)
    sage=forms.IntegerField()
    semail=forms.EmailField()
    saddr=forms.CharField()
    