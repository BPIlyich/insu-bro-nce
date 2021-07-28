from django.contrib.auth import get_user_model

from config.celery import app


User = get_user_model()


@app.task(ignore_result=True, max_retries=3)
def send_email_notification(user_id:int, subject: str, message: str) -> None:
    """
    Отправка оповещения страховой компании при создании отклика на продукт
    """
    User.objects.get(pk=user_id).email_user(subject, message)
