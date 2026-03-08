from django.urls import path
from wthehealth import views

urlpatterns = [
    path("", views.retrieve_data, name="retrieve_data"),
    path('average/', views.average, name='average'),
]