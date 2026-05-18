
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about-us/', views.AboutPageView.as_view(), name='about'),
    path('people/', views.PeoplePageView.as_view(), name='people'),
]
