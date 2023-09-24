from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('signup', views.signup, name='signup'),
    path('password_reset', views.password_reset, name='password_reset'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
    path('myprofile', views.myprofile, name='myprofile'),
    path('user_profile_edit', views.user_profile_edit, name='user_profile_edit'),
    path('add_employee', views.add_employee, name='add_employee'),
    path('emp_profile:<str:name>', views.emp_profile, name='emp_profile'),
    path('showall', views.showall, name='showall'),
    path('departments', views.departments, name='departments'),
    path('add_department', views.add_department, name='add_department'),
    path('click_department_data:<str:dept>', views.click_department_data, name='click_department_data'),
]
