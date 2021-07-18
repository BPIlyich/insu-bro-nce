from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


# На текущий момент полагаем, что каждый зарегистрированный пользователь - это
# отдельная страховая компания.
# Незарегистрированные пользователи - это потенциальные покупатели страховых
# продуктов.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Модель пользователя (страховой компании)
    """
    email = models.EmailField(_('email address'), unique=True)
    company_name = models.CharField(
        _('company name'), unique=True, max_length=200)
    is_staff = models.BooleanField(_('is staff'), default=False)
    is_active = models.BooleanField(_('is active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'company_name'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.company_name)

    class Meta:
        db_table = 'user'
        verbose_name = _('user')
        verbose_name_plural = _('users')
