from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _('email address'),
        max_length=128,
        unique=True,
        help_text=_(
            'Required. 128 characters or fewer. Letters, digits and @/./-/_ only.'
        ),
        error_messages={
            'unique': _('User with this email address already exists.'),
        },
    )
    first_name = models.CharField(_('first name'), max_length=128, blank=True)
    last_name = models.CharField(_('last name'), max_length=128, blank=True)
    password = models.CharField(_('password'), max_length=128)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether this user can log into this admin site.'
        ),
    )
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates whether this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_student = models.BooleanField(
        _('student status'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as student.'
        ),
    )
    is_teacher = models.BooleanField(
        _('teacher status'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as teacher.'
        ),
    )
    is_principal = models.BooleanField(
        _('principal status'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as principal.'
        ),
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
