from django.urls import include, path
from . import views
urlpatterns =[
    path('patient/', views.mainPatient, name='patient'),
    path('info_patient/<str:id>', views.infoPatient, name='info_patient'),
    path('modify_patient/<str:id>', views.modifyPatient, name='modify_patient'),
    path('register_history', views.registerHistory, name='register_history'),
    ]