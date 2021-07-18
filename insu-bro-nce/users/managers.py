from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where company_name is the unique identifier
    for authentication instead of usernames.
    """

    def create_user(self, company_name: str, password: str, **extra_fields):
        """
        Create and save a User with the given company_name and password.
        """
        if not company_name:
            raise ValueError(_('The company_name must be set'))
        user = self.model(company_name=company_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, company_name: str, password: str, **extra_fields):
        """
        Create and save a SuperUser with the given company_name and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(company_name, password, **extra_fields)
