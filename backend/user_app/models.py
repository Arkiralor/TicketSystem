
from datetime import timedelta
import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, RegexValidator
from django.db.models import Model, UUIDField, CharField, PositiveIntegerField, ForeignKey, EmailField, DateTimeField, SlugField, \
    BooleanField, TextField, OneToOneField, DateField, \
    CASCADE, SET_NULL, SET_DEFAULT
from django.template.defaultfilters import slugify
from django.utils import timezone

from user_app.constants import UserRegex


class User(AbstractUser):
    """
    Model to hold login/account information for a single 'User' entity.
    """

    id = UUIDField(
        primary_key=True,
        editable=False,
        unique=True,
        default=uuid.uuid4
    )
    
    first_name = CharField(max_length=16)
    last_name = CharField(max_length=16)
    regnal_number = PositiveIntegerField(blank=True, null=True)

    username = CharField(max_length=16, unique=True)
    email = EmailField(
        validators=[
            EmailValidator(
                message="Please enter a valid email address.",
                code="invalid_email"
            )
        ],
        unique=True
    )

    phone_primary = CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=UserRegex.PHONE_REGEX_IN,
                message="Please enter a valid phone number.",
                code="invalid_phone"
            )
        ],
        blank=True,
        null=True
    )

    unsuccessful_login_attempts = PositiveIntegerField(
        default=0,
        blank=True,
        null=True,
        help_text="Number of unsuccessful login attempts"
    )
    blocked_until = DateTimeField(
        blank=True,
        null=True,
        help_text="Blocked until"
    )

    slug = SlugField(blank=True, null=True)

    date_joined = DateTimeField(auto_now_add=True)
    date_modified = DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):

        self.slug = slugify(self.username)
        self.username = self.username.lower()
        self.email = self.email.lower()

        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        super(User, self).save(*args, **kwargs)

    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ("-date_joined", "date_modified")


class UserProfile(Model):
    """
    Table to hold Profile information about an User.
    """
    id = UUIDField(
        primary_key=True,
        editable=False,
        unique=True,
        default=uuid.uuid4
    )
    user = OneToOneField(User, on_delete=CASCADE)
    headline = CharField(max_length=128, blank=True, null=True, help_text="A bit about you in 128 characters or less.")
    about_me = TextField(blank=True, null=True)
    birthday = DateField(blank=True, null=True)
    location = CharField(max_length=64, blank=True, null=True)

    slug = SlugField(blank=True, null=True)

    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = self.user.slug
        super(UserProfile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
        ordering = (
            "-created",
            "-birthday"
        )