"""为应用程序users定义URL模式"""

from django.conf.urls import url
# from django.contrib.auth.views import LoginView 
from django.contrib.auth import views as auth_views

from . import views
app_name='users'

urlpatterns = [
	# 登录页面
	# url('login/', LoginView, {'template_name':'users/login.html'}, name='login')
	url(r'^login/$', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	# 注销
	url('logout/', views.logout_view, name='logout'),
	
	# 注册页面
	url('register/', views.register, name='register'),
]
