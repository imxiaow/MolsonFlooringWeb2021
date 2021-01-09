from django.urls import path
from . import views 


urlpatterns = [
    path('', views.homePage, name='home'),

    path('about/', views.aboutUs, name="about"), 
    path('product/', views.productPage, name="product"),
    path('services/', views.servicesPage, name="services"),
    path('gallery/', views.galleryPage, name="gallery"), 
    path('contact/', views.contactUs, name="contact"), 

]
