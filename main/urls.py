from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('email/', views.email, name="email"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="haqqımızda"),
    path('exams/', views.exams, name="exams"),
    path('gallery/', views.gallery, name="gallery"),
    path('career/', views.career, name="career"),
    path('xaricde_tehsil/', views.abroad, name="abroad"),
    path('dövlət_qulluğu/', views.civil_service, name="service"),
    path('sürücülük_sınaq/', views.driving, name="driving_exam"),
    path('imtahani_al/', views.details, name="details"),
    path('charge/', views.charge, name="charge"),
]