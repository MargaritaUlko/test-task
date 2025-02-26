# news/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils.timezone import localdate
from constance import config
from .models import News

@shared_task
def send_newsletter():
    """
    Отправляет email-рассылку с новостями за сегодня.
    """
    today = localdate()
    news_today = News.objects.filter(publication_date__date=today)

    if not news_today.exists():
        return "Нет новостей за сегодня."

    news_list = "\n".join([f"- {news.title}" for news in news_today])

    subject = config.NEWSLETTER_SUBJECT
    message = f"{config.NEWSLETTER_MESSAGE}\n{news_list}"
    recipient_list = [email.strip() for email in config.NEWSLETTER_RECIPIENTS.split(",") if email.strip()]

    if recipient_list:
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
        return f"Отправлено {len(recipient_list)} получателям."
    return "Нет адресатов для рассылки."
