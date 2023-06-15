from django.urls import path
from userauths.views import *

app_name ="userauths" 
urlpatterns = [
    path("signup", register_view, name='signup'),
    path("signin", login_view, name='signin'),
    path("signout", logout_view, name='signout'),
]
