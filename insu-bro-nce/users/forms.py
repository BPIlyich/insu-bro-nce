from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegisterForm(UserCreationForm):
    """
    Форма для регистрации пользователя (страховой компании)
    """
    class Meta:
        model = User
        fields = ('email', 'company_name')
