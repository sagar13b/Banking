from django.urls import path
from . import views

urlpatterns = [
    #path('rmanger/',views.register_manager,name='rm'),
    path('manager/login/',views.manager_login,name='aml'),
]