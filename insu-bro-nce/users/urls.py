from django.utils.translation import gettext_lazy as _
from django.urls import path, reverse_lazy
from django.contrib.auth import views

from .views import SignUpView, ProfileView

app_name = 'users'


urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('signup/', SignUpView.as_view(
        extra_context={'title': _('Sign Up')}
    ), name='signup'),
    path('login/', views.LoginView.as_view(
        template_name='users/login.html',
        extra_context={'title': _('Log in')}
    ), name='login'),
    path('logout/', views.LogoutView.as_view(
        template_name='users/logged_out.html',
        extra_context={'title': _('Logged out')}
    ), name='logout'),

    path('password_change/', views.PasswordChangeView.as_view(
        template_name='users/password_change_form.html',
        success_url = reverse_lazy(f'{app_name}:password_change_done')
    ), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html',
    ), name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(
        template_name='users/password_reset_form.html',
        success_url = reverse_lazy(f'{app_name}:password_reset_done')
    ), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html',
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html',
        success_url = reverse_lazy(f'{app_name}:password_reset_complete')
    ), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html',
    ), name='password_reset_complete'),
]
