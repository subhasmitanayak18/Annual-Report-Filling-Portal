from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import User, Role, Division

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ('email', 'role', 'is_staff', 'is_active', 'division')
    
    search_fields = ('email', 'role__role')
    
    # Order users by email
    ordering = ('email',)

    # Fields for viewing/editing user details
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('role', 'division')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    # Fields for the user creation form in admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'role', 'division', 'password1', 'password2'),
        }),
    )

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_id', 'role')
    search_fields = ('role',)

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('division_id', 'division')  # Adjust according to your model
    search_fields = ('division',)
    