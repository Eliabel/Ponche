from django.urls import re_path, path 
from . import views

app_name = "users"


urlpatterns = [
   	# Login, Register, Forgot password, Logout
    re_path(r'^login/$', views.LoginView.as_view(), name="login_url"),
    
    re_path(r'^logout/$', views.LogoutView.as_view(), name="logout_url"),

    re_path(r'^tables/$', views.TablesView.as_view(), name="tables_url"),

	re_path(r'^page_not_found/$', views.PageNotFoundView.as_view(), name="page_not_found_url"),    

	re_path(r'^blank/$', views.BlankView.as_view(), name="blank_page_url"),       

]