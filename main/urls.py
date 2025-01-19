from django.urls import path
from .views import CertificateDetailView,Index

urlpatterns = [
    path('certificate/5eafc947-e2cd-44a5-be62-45e97f294bae/<int:pk>/', CertificateDetailView.as_view(), name='certificate_detail'),
    path('certificate/',Index)
]
