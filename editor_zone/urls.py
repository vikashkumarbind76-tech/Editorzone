from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('services/', views.services_view, name='services'),
    path('service/<int:service_id>/', views.service_detail_view, name='service_detail'),
    path('booking/', views.booking_view, name='booking'),
    path('booking/<int:service_id>/', views.booking_view, name='booking_with_service'),
    path('confirmation/<int:booking_id>/', views.confirmation_view, name='confirmation'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('api/get-service-price/', views.get_service_price, name='get_service_price'),
]