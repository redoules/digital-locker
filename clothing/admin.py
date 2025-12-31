from django.contrib import admin
from .models import ClothingItem, UserProfile


@admin.register(ClothingItem)
class ClothingItemAdmin(admin.ModelAdmin):
    """Interface d'administration pour ClothingItem."""
    
    list_display = ('name', 'type', 'color', 'user', 'status', 'location', 'deposit_date')
    list_filter = ('type', 'status', 'deposit_date', 'user')
    search_fields = ('name', 'color', 'location', 'notes')
    date_hierarchy = 'deposit_date'
    ordering = ('-deposit_date',)
    
    fieldsets = (
        ('Informations principales', {
            'fields': ('user', 'name', 'type', 'color')
        }),
        ('Localisation et statut', {
            'fields': ('location', 'status', 'deposit_date')
        }),
        ('Détails supplémentaires', {
            'fields': ('photo', 'notes'),
            'classes': ('collapse',)
        }),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Interface d'administration pour UserProfile."""
    
    list_display = ('user', 'provider', 'avatar')
    list_filter = ('provider',)
    search_fields = ('user__username', 'user__email')
