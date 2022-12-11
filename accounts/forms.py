from django import forms
from django.contrib.auth import authenticate, password_validation
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import User


class LoginForm(forms.Form):
    email = forms.CharField(
        label=_('Email Address'),
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
        }),
    )
    password = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }),
    )

    error_messages = {
        'invalid_login': _(
            'Please enter a correct email address and password. '
            'Note that both fields may be case-sensitive.'
        ),
        'inactive': _('This account is inactive.'),
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)

            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(self.error_messages['inactive'], code='inactive')

    def get_invalid_login_error(self):
        return ValidationError(self.error_messages['invalid_login'], code='invalid_login')

    def get_user(self):
        return self.user_cache


class RegisterForm(forms.ModelForm):
    email = forms.CharField(
        label=_('Email Address'),
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
        }),
    )
    password1 = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }),
        help_text=(
            password_validation.password_validators_help_text_html(),
        ),
    )
    password2 = forms.CharField(
        label=_('Confirm Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        }),
        help_text=_(
            'Enter the same password as before, for verification.'
        ),
    )

    error_messages = {
        'password_mismatch': _('The two password fields did not match.'),
    }

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError(self.error_messages['password_mismatch'], code='password_mismatch')

        return password2

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get('password2')

        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)
