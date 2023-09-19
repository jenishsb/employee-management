from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('myprofile>', views.myprofile, name='myprofile'),
    path('user_profile_edit', views.user_profile_edit, name='user_profile_edit'),
    path('add_employee', views.add_employee, name='add_employee'),
    path('add_department', views.add_department, name='add_department'),
    path('emp_profile:<str:name>', views.emp_profile, name='emp_profile'),
    path('password_reset', views.password_reset, name='password_reset'),
    path('showall', views.showall, name='showall'),
    path('departments', views.departments, name='departments'),
    path('click_department_data:<str:dept>', views.click_department_data, name='click_department_data'),
    path('emp_department:<int:dept_name_id>:<str:emp>', views.emp_department, name='emp_department'),
    path('addresses', views.addresses, name='addresses'),
    path('address_edit:<str:emp>', views.address_edit, name='address_edit'),
    path('address_changed:<str:emp>', views.address_changed, name='address_changed'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
]
