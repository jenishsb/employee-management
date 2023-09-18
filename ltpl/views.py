from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from ltpl.forms import *
from django.contrib import messages
from ltpl.models import *


def index(request):
    login_form = CustomLoginForm()
    return render(request, 'login.html', {'form': login_form})


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


def homepage(request):
    return render(request, 'homepage.html')


def myprofile(request,  name):
    user = User.objects.get(first_name=name)
    form = User_profile(initial={'first_name': user.first_name, 'last_name': user.last_name, 'username': user.username, 'email': user.email})
    return render(request, 'myprofile.html', {'form': form, 'name': name})


def user_profile_edit(request, name):
    user = User.objects.get(first_name=name)
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


def emp_profile(request,  name):
    emp = Employee.objects.get(first_name=name)
    form = ProfileForm(initial={'first_name': emp.first_name, 'last_name': emp.last_name, 'username': emp.username, 'phno': emp.phno, 'email': emp.email})
    return render(request, 'emp_profile.html', {'form': form, 'name': name})


def showall(request):
    employees = Employee.objects.all()
    return render(request, 'showall.html', {'employees': employees})


def add_new_employee(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        form = Add_New_Employee(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Added Successfully...')
            return render(request, 'showall.html', {'employees': employees})
        else:
            pass
    form = Add_New_Employee()
    return render(request, 'add_new_employee.html', {'form': form})


def editdata(request, name):
    employees = Employee.objects.all()
    emp = Employee.objects.get(first_name=name)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=emp)
        if form.is_valid():
            if request.POST.get('update') == 'Update':
                form.save()
                messages.success(request, 'Data Updated Successfully...')
                print(f"---------- {user} ------------")
                return render(request, 'showall.html', {'employees': employees})
            elif request.POST.get('delete') == 'Delete':
                emp.delete()
                messages.success(request, 'Data Deleted Successfully...')
                return render(request, 'showall.html', {'employees': employees})
    form = ProfileForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})


def all_departments(request):
    all_departments = All_Departments.objects.all()
    return render(request, 'all_departments.html', {'all_departments': all_departments})


def add_new_department(request):
    all_departments = All_Departments.objects.all()
    if request.method == 'POST':
        form = Add_New_Department(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department Added Successfully...')
            return render(request, 'all_departments.html', {'all_departments': all_departments})
        else:
            pass
    form = Add_New_Department()
    return render(request, 'add_new_department.html', {'form': form})


def click_department_data(request, dept_name_id):
    all_departments = All_Departments.objects.all()
    click_department_data = Department.objects.get(name_id=dept_name_id)
    return render(request, 'click_department_data.html', {'all_departments': all_departments, 'department': click_department_data})


def emp_department(request, dept_name_id, emp):
    department = Department.objects.get(name_id=dept_name_id)
    employee = department.employees.get(first_name=emp)
    form = Department_change(initial={'name': department.name, 'employees': employee})
    return render(request, 'department_change.html', {'form': form, 'dept_name_id': dept_name_id, 'employee': emp})


def mydepartment_changed(request, dept_name_id, emp):
    departments = Department.objects.all()
    old_department = get_object_or_404(Department, name_id=dept_name_id)
    if request.method == 'POST':
        form = Department_change(request.POST, instance=old_department)
        if form.is_valid():
            if request.POST.get('update') == 'Update':
                departmentchange = form.cleaned_data['name']
                employeechange = form.cleaned_data['employees']  # Get the selected employees

                existing_employees = old_department.employees.all()

                try:
                    change_department = Department.objects.get(name=departmentchange)

                    for empchange in employeechange:
                        for employee in existing_employees:
                            if empchange.first_name != employee.first_name:
                                old_department.employees.add(employee)
                            else:
                                change_department.employees.add(employee)
                                old_department.employees.remove(employee)

                except Department.DoesNotExist:
                    try:
                        get_department = All_Departments.objects.get(department_name=departmentchange)

                        create_department = Department.objects.create(name=get_department)

                        for empchange in employeechange:
                            for employee in existing_employees:
                                if empchange.first_name != employee.first_name:
                                    old_department.employees.add(employee)
                                else:
                                    create_department.employees.add(employee)
                                    old_department.employees.remove(employee)
                    except All_Departments.DoesNotExist:
                        pass

                messages.success(request, 'Data Updated Successfully...')
                return render(request, 'homepage.html', {'logged_user': user})
    else:
        form = Department_change(instance=old_department)

    return render(request, 'department_change.html', {'form': form, 'dept_name_id': dept_name_id, 'employee': emp})


def addresses(request):
    emp_addresses = Address.objects.all()
    return render(request, 'emp_addresses.html', {'user': emp_addresses})


def address_edit(request, emp):
    emp_address = Address.objects.get(employee_id=emp)
    form = Address_change(initial={'employee': emp, 'street': emp_address.street, 'city': emp_address.city, 'state': emp_address.state, 'zipcode': emp_address.zipcode})
    return render(request, 'address_edit.html', {'form': form, 'employee': emp})


def address_changed(request, emp):
    emp_addresses = Address.objects.all()
    emp_address = Address.objects.get(employee_id=emp)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=emp_address)
        if form.is_valid():
            if request.POST.get('update') == 'Update':
                form.save()
                messages.success(request, 'Data Updated Successfully...')
                return render(request, 'showall.html', {'user': emp_addresses})
    else:
        pass
    form = Address_change(initial={'employee': emp, 'street': emp_address.street, 'city': emp_address.city, 'state': emp_address.state, 'zipcode': emp_address.zipcode})
    return render(request, 'address_edit.html', {'form': form, 'employee': emp})


def logoutuser(request):
    logout(request)
    global user
    user = None
    messages.success(request, "User Logged Out Successfully...")
    return redirect('login')
