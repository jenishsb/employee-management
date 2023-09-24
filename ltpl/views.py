from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from ltpl.forms import *
from django.contrib import messages
from ltpl.models import *


def index(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    login_form = CustomLoginForm()
    return render(request, 'login.html', {'form': login_form})


def homepage(request):
    return render(request, 'homepage.html')


def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            global user
            user = authenticate(request, username=username, password=password)
            print(f"Authenticated User: {user}")
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Successfully...')
                return render(request, 'homepage.html', {'logged_user': user})
            else:
                pass
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Created Successfully...')
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})



def myprofile(request):
    user = User.objects.get(username=request.user)
    form = User_profile(initial={'first_name': user.first_name, 'last_name': user.last_name, 'username': user.username, 'email': user.email})
    return render(request, 'myprofile.html', {'form': form})


def user_profile_edit(request):
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = User_profile(request.POST, instance=user)
        if form.is_valid():
            if request.POST.get('update') == 'Update':
                form.save()
                messages.success(request, 'User Data Updated Successfully...')
                return render(request, 'homepage.html')
            elif request.POST.get('delete') == 'Delete':
                user.delete()
                messages.success(request, 'User Deleted Successfully...')
                return redirect('login')
    form = User_profile(instance=user)
    return render(request, 'myprofile.html', {'form': form})


def showall(request):
    employees = Employee.objects.all()
    return render(request, 'showall.html', {'employees': employees})


def add_employee(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        form = Add_Employee(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Added Successfully...')
            return render(request, 'showall.html', {'employees': employees})
        else:
            pass
    form = Add_Employee()
    return render(request, 'add_employee.html', {'form': form})


def emp_profile(request, name):
    employees = Employee.objects.all()
    emp = Employee.objects.get(first_name=name)
    if request.method == 'POST':
        form = Emp_ProfileForm(request.POST, instance=emp)
        if form.is_valid():
            if request.POST.get('update') == 'Update':
                form.save()
                messages.success(request, 'Data Updated Successfully...')
                return render(request, 'showall.html', {'employees': employees})
            elif request.POST.get('delete') == 'Delete':
                emp.delete()
                messages.success(request, 'Data Deleted Successfully...')
                return render(request, 'showall.html', {'employees': employees})
    form = Emp_ProfileForm(instance=emp)
    return render(request, 'emp_profile.html', {'form': form})


def departments(request):
    departments = Departments.objects.all()
    return render(request, 'departments.html', {'departments': departments})


def click_department_data(request,dept):
    departments = Departments.objects.all()
    department = Departments.objects.filter(department_name=dept)
    employees = Employee.objects.filter(department_id=dept)
    return render(request, 'departments.html', {'departments': departments, 'department': department[0], 'employees': employees})


def add_department(request):
    departments = Departments.objects.all()
    if request.method == 'POST':
        form = Add_Department(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department Added Successfully...')
            return render(request, 'departments.html', {'departments': departments})
        else:
            pass
    form = Add_Department()
    return render(request, 'add_department.html', {'form': form})


def logoutuser(request):
    logout(request)
    global user
    user = None
    messages.success(request, "User Logged Out Successfully...")
    return redirect('login')


@login_required
def password_reset(request):
    if request.method == 'POST':
        form = Change_password(user=request.user, data=request.POST)
        if form.is_valid():
            logged_user = form.save()
            # Update the session auth hash to keep the user logged in
            update_session_auth_hash(request, logged_user)
            messages.success(request, 'Your password has been successfully changed.')
            return redirect('login')
    else:
        form = Change_password(user=request.user)

    return render(request, 'password_change.html', {'form': form})
