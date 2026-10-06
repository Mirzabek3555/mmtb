from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('haqida/', views.about, name='about'),
    path('hujjatlar/', views.documents, name='documents'),
    path('elon/<int:pk>/', views.announcement_detail, name='announcement_detail'),
]
