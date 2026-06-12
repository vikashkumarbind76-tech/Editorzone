from django.contrib import admin
from .models import UserProfile, Service, Portfolio, Booking, Contact

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'company', 'created_at')
    search_fields = ('user__username', 'user__email', 'phone', 'company')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'package_type', 'price', 'delivery_time', 'is_active')
    list_filter = ('package_type', 'is_active')
    search_fields = ('name', 'description')
    list_editable = ('price', 'is_active')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_type', 'completion_time', 'is_featured', 'created_at')
    list_filter = ('project_type', 'is_featured')
    search_fields = ('title', 'client_name')
    list_editable = ('is_featured',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'user', 'service', 'total_cost', 'status', 'created_at')
    list_filter = ('status', 'service__package_type')
    search_fields = ('project_title', 'user__username', 'service__name')
    list_editable = ('status',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_editable = ('is_read',)