from django.urls import include, path
from . import views
urlpatterns =[
    path('register_patient/', views.registerPatient, name='register_patient'),
    path('patient/', views.mainPatient, name='patient'),
    path('info_patient/<str:id>', views.infoPatient, name='info_patient'),
    path('modify_patient/<str:id>', views.modifyPatient, name='modify_patient')

]