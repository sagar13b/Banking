from django.urls import path
from . import views

urlpatterns = [
    path('rmanger/',views.register_manager,name='rm'),
]