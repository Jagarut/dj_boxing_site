
from django.shortcuts import render
from .models import Fighter, Event, News, Testimonial

def home(request):
    # Retrieve featured matches/events and latest news for the home page
    featured_events = Event.objects.all().order_by('-date')[:3]  # Example: Showing 3 latest events
    latest_news = News.objects.all().order_by('-created_at')[:3]  # Example: Showing 3 latest news articles

    context = {
        'featured_events': featured_events,
        'latest_news': latest_news,
    }
    return render(request, 'gimnasio/home.html', context)

def about(request):
    return render(request, 'gimnasio/about.html')

