# create this file manually

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage', views.homepage, name='homepage'),
    path('signup', views.signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('myprofile:<str:name>', views.myprofile, name='myprofile'),
    path('user_profile_edit:<str:name>', views.user_profile_edit, name='user_profile_edit'),
    path('add_new_employee', views.add_new_employee, name='add_new_employee'),
    path('add_new_department', views.add_new_department, name='add_new_department'),
    path('emp_profile:<str:name>', views.emp_profile, name='emp_profile'),
    path('password_reset', views.password_reset, name='password_reset'),
    path('showall', views.showall, name='showall'),
    path('all_departments', views.all_departments, name='all_departments'),
    path('click_department_data:<int:dept_name_id>', views.click_department_data, name='click_department_data'),
    path('emp_department:<int:dept_name_id>:<str:emp>', views.emp_department, name='emp_department'),
    path('addresses', views.addresses, name='addresses'),
    path('address_edit:<str:emp>', views.address_edit, name='address_edit'),
    path('address_changed:<str:emp>', views.address_changed, name='address_changed'),
    path('editdata:<str:name>', views.editdata, name='editdata'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
]
