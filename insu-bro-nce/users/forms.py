from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth import get_user_model

from .tasks import send_mail


User = get_user_model()


class UserRegisterForm(UserCreationForm):
    """
    Форма для регистрации пользователя (страховой компании)
    """
    class Meta:
        model = User
        fields = ('email', 'company_name')


class PasswordResetTaskForm(PasswordResetForm):
    """
    Переопределенная стандартная форма для восстановления пароля.
    Отправка письма происходит через очередь задач
    """

    def send_mail(self, subject_template_name, email_template_name, context,
                  from_email, to_email, html_email_template_name=None):
        """
        Отправка письма через очередь задач
        """
        context['user'] = context['user'].id

        send_mail.delay(subject_template_name, email_template_name, context,
                        from_email, to_email, html_email_template_name)
