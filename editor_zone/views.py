from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import UserProfile, Service, Portfolio, Booking, Contact
import json
from decimal import Decimal
from datetime import datetime

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone', '')
        company = request.POST.get('company', '')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'signup.html')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        profile = UserProfile.objects.create(user=user, phone=phone, company=company)
        
        messages.success(request, 'Account created successfully! Please log in.')
        return redirect('login')
    
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def home_view(request):
    featured_portfolio = Portfolio.objects.filter(is_featured=True)[:4]
    services = Service.objects.filter(is_active=True)[:4]
    context = {
        'featured_portfolio': featured_portfolio,
        'services': services,
    }
    return render(request, 'home.html', context)

def portfolio_view(request):
    portfolio_items = Portfolio.objects.all().order_by('-created_at')
    return render(request, 'portfolio.html', {'portfolio_items': portfolio_items})

def services_view(request):
    basic_services = Service.objects.filter(package_type='basic', is_active=True)
    professional_services = Service.objects.filter(package_type='professional', is_active=True)
    premium_services = Service.objects.filter(package_type='premium', is_active=True)
    
    context = {
        'basic_services': basic_services,
        'professional_services': professional_services,
        'premium_services': premium_services,
    }
    return render(request, 'services.html', context)

def service_detail_view(request, service_id):
    service = get_object_or_404(Service, id=service_id, is_active=True)
    return render(request, 'service_detail.html', {'service': service})

@login_required
def booking_view(request, service_id=None):
    if request.method == 'POST':
        service_id = request.POST.get('service_id')
        project_title = request.POST.get('project_title')
        project_description = request.POST.get('project_description')
        deadline = request.POST.get('deadline')
        special_requirements = request.POST.get('special_requirements', '')
        
        service = get_object_or_404(Service, id=service_id, is_active=True)
        
        booking = Booking.objects.create(
            user=request.user,
            service=service,
            project_title=project_title,
            project_description=project_description,
            deadline=deadline,
            total_cost=service.price,
            special_requirements=special_requirements
        )
        
        return redirect('confirmation', booking_id=booking.id)
    
    service = None
    if service_id:
        service = get_object_or_404(Service, id=service_id, is_active=True)
    
    services = Service.objects.filter(is_active=True)
    return render(request, 'booking.html', {'services': services, 'selected_service': service})

@login_required
def confirmation_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    return render(request, 'confirmation.html', {'booking': booking})

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        company = request.POST.get('company', '')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            company=company,
            subject=subject,
            message=message
        )
        
        messages.success(request, 'Your message has been sent successfully! We will contact you soon.')
        return redirect('contact')
    
    return render(request, 'contact.html')

@csrf_exempt
def get_service_price(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        service_id = data.get('service_id')
        
        try:
            service = Service.objects.get(id=service_id, is_active=True)
            return JsonResponse({
                'price': float(service.price),
                'delivery_time': service.delivery_time,
                'name': service.name
            })
        except Service.DoesNotExist:
            return JsonResponse({'error': 'Service not found'}, status=404)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)