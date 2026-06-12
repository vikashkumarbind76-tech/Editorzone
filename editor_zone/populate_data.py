import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'editor_zone.settings')
import django
django.setup()

from main.models import Service, Portfolio

# Clear existing data
Service.objects.all().delete()
Portfolio.objects.all().delete()

# Create Services
services_data = [
    # Basic
    {"name": "Basic Cut & Trim", "description": "Essential editing for clean, professional footage.", "package_type": "basic", "price": 1499.00, "delivery_time": "3-5 days", "features": "Basic cuts, Color correction, Audio cleanup, Simple transitions"},
    {"name": "YouTube Ready Basic", "description": "Perfect for YouTube and social media videos.", "package_type": "basic", "price": 2499.00, "delivery_time": "4-6 days", "features": "Custom thumbnails, Text overlays, Music sync, End screens"},
    {"name": "Short Video Edit", "description": "TikTok, Reels, and Shorts editing.", "package_type": "basic", "price": 999.00, "delivery_time": "2-3 days", "features": "Fast cuts, Trending effects, Text animation, Optimized export"},
    # Professional
    {"name": "Corporate Video Pro", "description": "Professional business and corporate videos.", "package_type": "professional", "price": 9999.00, "delivery_time": "7-10 days", "features": "Advanced grading, Motion graphics, Voiceover sync, Brand kit"},
    {"name": "Wedding Highlights Pro", "description": "Emotional wedding montages and highlights.", "package_type": "professional", "price": 14999.00, "delivery_time": "8-12 days", "features": "Cinematic grading, Music selection, Slow motion, Emotional flow"},
    {"name": "Product Demo Pro", "description": "High-conversion product demo videos.", "package_type": "professional", "price": 7999.00, "delivery_time": "6-8 days", "features": "3D elements, Screen recordings, CTA overlays, A/B variants"},
    # Premium
    {"name": "Music Video Premium", "description": "Artist-grade music video production.", "package_type": "premium", "price": 24999.00, "delivery_time": "14-21 days", "features": "VFX, Advanced compositing, Custom graphics, Unlimited revisions"},
    {"name": "Commercial Ad Premium", "description": "Broadcast-ready TV commercials.", "package_type": "premium", "price": 39999.00, "delivery_time": "15-20 days", "features": "Full production, Talent integration, Multiple formats, TV specs"},
    {"name": "Documentary Premium", "description": "Feature-length documentary editing.", "package_type": "premium", "price": 74999.00, "delivery_time": "30+ days", "features": "Multi-cam sync, Archival footage, Interviews, Narrative structure"},
]

for data in services_data:
    Service.objects.create(**data)

print(f"Created {Service.objects.count()} Services")

# Create Portfolio
portfolio_data = [
    {"title": "Modern Corporate Brand Launch", "project_type": "Corporate Video Pro", "completion_time": "7 days", "image_url": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=400", "description": "Dynamic brand launch video for a tech startup with high-end motion graphics and testimonials.", "client_name": "TechCorp", "is_featured": True},
    {"title": "Cinematic Wedding Highlights", "project_type": "Wedding Highlights Pro", "completion_time": "10 days", "image_url": "https://images.unsplash.com/photo-1519741497674-611481863552?w=400", "description": "Emotional wedding highlight reel featuring professional cinematic color grading and audio mix.", "client_name": "Sharma Family", "is_featured": True},
    {"title": "Vlog Cut & Trim Showreel", "project_type": "Basic Cut & Trim", "completion_time": "3 days", "image_url": "https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?w=400", "description": "Clean video cuts, audio noise cleanup, and basic color correction for travel vlogs.", "client_name": "Vlog Diaries", "is_featured": True},
    {"title": "Tech Review Video Production", "project_type": "YouTube Ready Basic", "completion_time": "5 days", "image_url": "https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?w=400", "description": "High-quality YouTube video with transitions, end screens, title animations, and background music.", "client_name": "GizmoHQ", "is_featured": False},
    {"title": "Fast-Paced Shorts/Reels Bundle", "project_type": "Short Video Edit", "completion_time": "2 days", "image_url": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=400", "description": "Bundle of 5 vertical short-form videos with trending subtitles, sound FX, and zoom transitions.", "client_name": "FitStyle Co.", "is_featured": True},
    {"title": "Wireless Earbuds Product Promo", "project_type": "Product Demo Pro", "completion_time": "6 days", "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400", "description": "High-conversion product showcase showing core features with 3D text tracking and smooth pans.", "client_name": "SoundWave Ltd.", "is_featured": False},
    {"title": "'Midnight Melody' Indie Music Video", "project_type": "Music Video Premium", "completion_time": "14 days", "image_url": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=400", "description": "Premium grade music video with advanced composite overlays, green screen keying, and VFX coloring.", "client_name": "Ritika Sen (Artist)", "is_featured": True},
    {"title": "National TV Ad - 'Quench Juice'", "project_type": "Commercial Ad Premium", "completion_time": "18 days", "image_url": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400", "description": "Broadcast-ready ad spot editing with professional grading, voiceover integrations, and legal overlays.", "client_name": "Quench Beverages", "is_featured": True},
    {"title": "Mini-Documentary - 'Echoes of the Wild'", "project_type": "Documentary Premium", "completion_time": "25 days", "image_url": "https://images.unsplash.com/photo-1473163928189-364b2c4e1135?w=400", "description": "Compelling narrative documentary edit combining multiple field cameras and historical stock footage.", "client_name": "WildLife Trust India", "is_featured": True},
]

for data in portfolio_data:
    Portfolio.objects.create(**data)

print(f"Created {Portfolio.objects.count()} Portfolio items")

print("Data populated successfully! Refresh your browser.")

