from django.urls import path
from . import views

app_name = "admissions"

urlpatterns = [
    path("", views.AdmissionPageView.as_view(), name="list"),
]