from django.urls import path
from . import views

app_name = 'schools'

urlpatterns = [
    path('', views.school_list, name='list'),
    path('<int:pk>/', views.school_detail, name='detail'),
]
