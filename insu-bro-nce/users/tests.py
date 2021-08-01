from django.test import TestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserTests(TestCase):
    """
    Тесты для кастомной модели пользователя (страховой компании)
    """

    def test_create_user(self):
        """
        Тесты создания обычного пользователя
        """
        user = User.objects.create_user(
            company_name='company_name',
            email='user@example.com',
            password='user_password'
        )
        self.assertEqual(user.email, 'user@example.com')
        self.assertEqual(user.company_name, 'company_name')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(TypeError):
            User.objects.create_user(company_name='')
        with self.assertRaises(ValueError):
            User.objects.create_user(
                company_name='',
                email='',
                password='user_password'
            )

    def test_create_superuser(self):
        """
        Тесты создания суперпользователя
        """
        admin_user = User.objects.create_superuser(
            company_name='company_name',
            email='admin@example.com',
            password='admin_password'
        )
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                company_name='company_name',
                email='admin@example.com',
                password='admin_password',
                is_superuser=False
            )
