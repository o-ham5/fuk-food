import uuid
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, _user_has_perm
)
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class AccountManager(BaseUserManager):
    def create_user(self, request_data, **kwargs):
        now = timezone.now()
        if not request_data['email']:
            raise ValueError('Users must have an email address.')

        user = self.model(
            username=request_data['username'],
            email=self.normalize_email(request_data['email']),
            is_active=True,
            last_login=now,
            date_joined=now,
        )

        # AbstractBaseUserのメソッドを使ってパスワードを付与
        user.set_password(request_data['password'])
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        request_data = {
            'username': username,
            'email': email,
            'password': password
        }
        user = self.create_user(request_data)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        # user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    account_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(_('username'), max_length=30, unique=True)
    email = models.EmailField(verbose_name='email address',
                              max_length=255, unique=True)
    bias = models.FloatField(default=0)
    variance = models.FloatField(default=0)
    evals = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def user_has_perm(user, perm, obj):
        return _user_has_perm(user, perm, obj)

    def has_perm(self, perm, obj=None):
        return _user_has_perm(self, perm, obj=obj)

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    class Meta:
        db_table = 'accounts'
        swappable = 'AUTH_USER_MODEL'
