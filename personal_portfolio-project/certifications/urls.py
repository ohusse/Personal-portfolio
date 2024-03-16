from django.urls import path
from . import views

app_name = 'certifications'

urlpatterns = [
    path('', views.all_certifications, name='all_certifications'),
]
