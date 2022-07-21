from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User, UserCity, City


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('phone', 'otp', 'is_staff', 'is_superuser')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('phone',)
    search_fields = ('first_name', 'last_name', 'phone', 'otp')  # 🖘 no username
    fieldsets = (
        (
            'Fields',
            {
                'fields': (
                    'phone',
                    'date_joined',
                    'last_login',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                    'password',
                )
            },
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'otp', 'password1', 'password2'),
            #              🖞 without username
        }),
    )


admin.site.register(User, CustomUserAdmin)


admin.autodiscover()


admin.site.register(UserCity)
admin.site.register(City)
