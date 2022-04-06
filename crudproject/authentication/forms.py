from cProfile import label
from django.contrib.auth.models import User
from django import  forms
from django.contrib.auth.forms import UserCreationForm
from .models import Books

class SignUpForm(UserCreationForm):
    password2 =forms.CharField(label ='Confirm Password',widget=forms.PasswordInput())
    phone_number = forms.CharField(label ='Phone Number',widget=forms.NumberInput())
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}
        

class BooksRegistration(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['book_name','author','price','category']
        widgets = {
            'book_name':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'published_on': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            
        }
