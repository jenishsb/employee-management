from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from ltpl.models import *


GENDER_CHOICES = (
        ('Select', '--- Select Gender ---'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Enter Username'}), label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}), label="")


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
        label=""
    )
    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
        label=""
    )
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
        label=""
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
        label=""
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
        label=""
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}),
        label=""
    )


class User_profile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
        label="First Name:"
    )
    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
        label="Last Name:"
    )
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
        label="Username:"
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
        label="Email:"
    )


class Change_password(PasswordChangeForm):
    class Meta:
        model = User
        fields = []

    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter old password'}),
        label=""
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'}),
        label=""
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password again'}),
        label=""
    )


class Add_Employee(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), label='')
    department = forms.ModelChoiceField(queryset=Departments.objects.all(), empty_label='--- Select Department ---', widget=forms.Select(attrs={'class': 'form-control'}), label='')

    class Meta:
        model = Employee
        fields = "__all__"
        labels = {
            'first_name': '',
            'last_name': '',
            'phno': '',
            'email': '',
            'username': '',
            'password': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'phno': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone No'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Create Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Create Password'})
        }


class Emp_ProfileForm(Add_Employee):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'gender', 'phno', 'email', 'username', 'department']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'phno': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone No'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Create Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Create Password'})
        }

class Add_Department(forms.ModelForm):
    class Meta:
        model = Departments
        fields = "__all__"
        labels = {
            'name': ''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add New Department'})
        }
