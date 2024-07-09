from django.forms import TextInput,EmailInput,NumberInput
from django import forms
from .models import Cart




class OrderForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ["name","place","email","address","city","phonenumber"] 
        widgets = {
            'name' : TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name',
            }),
            'place' : TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder' : 'Enter your place',
            }),
            'email' : EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder' : 'Enter your email',
            }),
            'address' : TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder' : 'Enter your addres'
            }),
            'city' : TextInput(attrs={
               'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder' : 'Enter your city'
            }),
            'phonenumber' : TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder' : 'Enter your mobile number'
            }),
        }
        
    #name=forms.CharField(label="enter your name",max_length=20)
   #place=forms.CharField(label="enter yor place",max_length=100)
    #phone=forms.IntegerField(label="enter your mobile number")
    #address=forms.CharField(label="enter your address")
    

