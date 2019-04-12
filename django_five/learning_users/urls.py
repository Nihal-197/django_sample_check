
from django.urls import path
from learning_users import views

app_name= 'learning_users'

urlpatterns=[
    path('register',views.register,name='register'),
    path('user_login',views.user_login,name='user_login')

]
