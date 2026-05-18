
from django.urls import path
from . import views

app_name = 'branches'

urlpatterns = [
    path('', views.BranchListView.as_view(), name='list'),
    path('boys-campus/', views.BranchListView.as_view(), {'campus_type': 'boys'}, name='boys'),
    path('girls-campus/', views.BranchListView.as_view(), {'campus_type': 'girls'}, name='girls'),
    path('<slug:slug>/', views.BranchDetailView.as_view(), name='detail'),
]
