from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = "account_api"

urlpatterns = [
    path('user/', views.getUser_view.as_view(), name='get_user'),
    path('register', views.register_view.as_view(), name='register_user'),
    path('login', views.login_view.as_view(), name='login_user'),
    path('auth/', include('dj_rest_auth.urls', namespace='djrest_api')),





    

]