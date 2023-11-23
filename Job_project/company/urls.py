from django.urls import path
from . import views

urlpatterns = [
    path('update-company/', views.update_company, name = 'update-company'),
    path('create-company/', views.create_company, name = 'create-company'),
    path('company-details/<int:pk>', views.company_details, name = 'company-details')

]