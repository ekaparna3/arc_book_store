from bookstoreapp.models import BookModel
from django import forms
from django.contrib.auth.models import User


class BookForm(forms.Form):
    title=forms.CharField(max_length=200)
    price=forms.IntegerField()
    author=forms.CharField(max_length=200)
    description=forms.CharField(max_length=500)
    image=forms.ImageField()
    
class RegisterForm(forms.Form):
    first_name=forms.CharField(max_length=200)
    last_name=forms.CharField(max_length=200)
    username=forms.CharField(max_length=200)
    password=forms.PasswordInput()

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","password"]

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]

class SearchForm(forms.Form):
    searched=forms.CharField(label='Search',max_length=100)
    