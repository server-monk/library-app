import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField
from users.managers import CustomManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    '''
    Overrides django's default `User()` model. Removes `username` field.
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=500)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True, help_text="Use the format: +(country) eg +2347000000123")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CustomManager()

    USERNAME_FIELD = 'email' # allow sign up and login with email instead of default username
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


    def __str__(self):
        return self.get_full_name() + '-' + self.get_email()

    def get_full_name(self):
        return self.first_name +' '+ self.last_name

    def get_short_name(self):
        return self.first_name

    def get_email(self):
        return self.email

