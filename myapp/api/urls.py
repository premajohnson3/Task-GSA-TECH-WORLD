from django.urls import path
from .views import register, login, dashboard, add_task, logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add_task/', add_task, name='add_task'),
    path('logout/', logout, name='logout'),
]
