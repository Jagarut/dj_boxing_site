from django.contrib import admin
from .models import Fighter, Event, News, Testimonial

# Register your models here

@admin.register(Fighter)
class FighterAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'weight_class')
    search_fields = ('name', 'nationality')
    # Other configurations for Fighter model in admin panel

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'venue')
    search_fields = ('title', 'venue')
    # Other configurations for Event model in admin panel

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author')
    # Other configurations for News model in admin panel

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'occupation', 'created_at')
    search_fields = ('name', 'occupation')
    # Other configurations for Testimonial model in admin panel

