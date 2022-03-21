from click import option
from django import forms

Gender_CHOICES= [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other','Other'),
]
# hobbies=[
#     ('Drawing'),('Singing'),('Dancing'),('Others')
# ]

class studentForms(forms.Form):
    FIRST_NAME=forms.CharField(max_length=30)
    LAST_NAME=forms.CharField(max_length=30)
    # DATE_OF_BIRTH=forms.DateField()
    EMAIL_ID=forms.EmailField()
    PHONE_NO=forms.IntegerField(max_value=10)
    GENDER=forms.CharField(label='Gender',widget=forms.RadioSelect(choices=Gender_CHOICES))
    STATE=forms.CharField(max_length=20)
    CITY=forms.CharField(max_length=20)
    PIN=forms.IntegerField(max_value=6)
    ADDRESS=forms.CharField(max_length=100)
    # HOBBIES=forms.(choices=hobbies)
    
    
    