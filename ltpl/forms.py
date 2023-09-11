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


class Add_New_Employee(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), label='')

    class Meta:
        model = Employee
        fields = "__all__"
        labels = {
            'first_name': '',
            'last_name': '',
            'username': '',
            'phno': '',
            'email': '',
            'password': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Create Username'}),
            'phno': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone No'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Create Password'})
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'username', 'phno', 'email']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'phno': 'Phone No',
            'email': 'Email',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Create Username'}),
            'phno': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone No'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'})
        }

class Add_New_Department(forms.ModelForm):
    class Meta:
        model = All_Departments
        fields = "__all__"
        labels = {
            'name': ''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add New Department'})
        }

class Department_change(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
        labels = {
            'name': 'Department',
            'employees': 'Employee Name'
        }

class Address_change(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
        labels = {
            'employee': 'Employee Name',
            'street': 'Street',
            'city': 'City',
            'state': 'State',
            'zipcode': 'Zipcode'
        }
        widgets = {
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'})
        }
