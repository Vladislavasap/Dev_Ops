import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    USER_ROLES = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    ]
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(
        validators=[UnicodeUsernameValidator(), ],
        max_length=150,
        unique=True,
    )
    email = models.EmailField(
        unique=True,
        max_length=254,
        verbose_name='email'
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
    )
    bio = models.TextField(
        verbose_name='about me',
        blank=True
    )
    role = models.CharField(
        max_length=128,
        choices=USER_ROLES,
        default=USER,
    )
    confirmation_code = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        blank=True
    )
    password = models.CharField(
        blank=True,
        max_length=128
    )

    @property
    def is_user(self):
        return self.role == self.USER

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    class Meta:
        verbose_name = 'Пользователи'
        ordering = ('id',)
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_username_email',)
        ]

    def __str__(self):
        return self.username
