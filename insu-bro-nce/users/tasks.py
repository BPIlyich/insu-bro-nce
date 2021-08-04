from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm

from config.celery import app


User = get_user_model()


@app.task(ignore_result=True, max_retries=3)
def send_mail(subject_template_name, email_template_name, context, from_email,
              to_email, html_email_template_name=None):
    """
    Копия метода send_mail класса django.contrib.auth.forms.PasswordResetForm
    для отправки письма на восстановление пароля через очередь задач
    """
    context['user'] = User.objects.get(pk=context['user'])

    PasswordResetForm.send_mail(
        None,
        subject_template_name=subject_template_name,
        email_template_name=email_template_name,
        context=context,
        from_email=from_email,
        to_email=to_email,
        html_email_template_name=html_email_template_name
    )
