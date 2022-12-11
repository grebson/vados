from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import UserCreateForm, UserUpdateForm
from .models import User


class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                'fields': ('email', 'password1', 'password2'),
            },
        ),
    )
    add_form = UserCreateForm
    exclude = ('username',)
    fieldsets = (
        (
            None,
            {
                'fields': ('email', 'password'),
            },
        ),
        (
            _('Personal info'),
            {
                'fields': ('first_name', 'last_name'),
            },
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (
            _('Important dates'),
            {
                'fields': ('last_login', 'date_joined'),
            },
        ),
        (
            _('School related info'),
            {
                'fields': ('is_student', 'is_teacher', 'is_principal')
            },
        ),
    )
    filter_horizontal = ('groups', 'user_permissions')
    form = UserUpdateForm
    list_display = ('email', 'first_name', 'last_name', 'is_student', 'is_teacher', 'is_principal')
    ordering = ('email',)
    search_fields = ('email', 'first_name', 'last_name')


admin.site.register(User, UserAdmin)
