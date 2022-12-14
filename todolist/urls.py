from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name="show_todolist"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('create-task/', show_create_page, name='show_create_page'),
    path('add/', show_create_page, name='show_create_page'),
    path('json/', todolist_json, name='todolist_json'),
    path('show/json/', show_todolist_ajax, name='show_todolist_ajax')
]