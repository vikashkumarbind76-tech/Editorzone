from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect
from .models import Service, Portfolio

def home_view(request):
    """Home page with hero section and featured content."""
    portfolios = Portfolio.objects.filter(is_featured=True)[:6]
    return render(request, 'home.html', {'portfolios': portfolios})

def services_view(request):
    """Services page with packages categorized by type."""
    basic_services = Service.objects.filter(package_type='basic', is_active=True)
    professional_services = Service.objects.filter(package_type='professional', is_active=True)
    premium_services = Service.objects.filter(package_type='premium', is_active=True)
    return render(request, 'services.html', {
        'basic_services': basic_services,
        'professional_services': professional_services,
        'premium_services': premium_services
    })

def service_detail_view(request, service_id):
    """Detailed view of a specific service."""
    service = get_object_or_404(Service, id=service_id, is_active=True)
    return render(request, 'service_detail.html', {'service': service})

def booking_view(request, service_id=None):
    """Booking form page."""
    services = Service.objects.filter(is_active=True)
    selected_service = None
    if service_id:
        selected_service = get_object_or_404(Service, id=service_id, is_active=True)
    return render(request, 'booking.html', {
        'services': services,
        'selected_service': selected_service
    })

def confirmation_view(request, booking_id):
    """Booking confirmation page."""
    # Stub: In full app, fetch Booking by id
    return render(request, 'confirmation.html', {'booking_id': booking_id})

def portfolio_view(request):
    """Portfolio showcase."""
    portfolios = Portfolio.objects.all().order_by('-created_at')
    return render(request, 'portfolio.html', {'portfolios': portfolios})

def about_view(request):
    """About us page."""
    return render(request, 'about.html')

def contact_view(request):
    """Contact page."""
    return render(request, 'contact.html')

def login_view(request):
    """User login."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    """User signup."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    """User logout."""
    logout(request)
    return redirect('home')

def get_service_price(request):
    """API endpoint for service pricing (used by JS)."""
    if request.method == 'POST':
        service_id = request.POST.get('service_id')
        try:
            service = Service.objects.get(id=service_id)
            return JsonResponse({
                'price': str(service.price),
                'delivery_time': service.delivery_time
            })
        except Service.DoesNotExist:
            pass
    return JsonResponse({'error': 'Service not found'}, status=404)

