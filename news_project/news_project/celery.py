# news_project/celery.py
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_project.settings')

app = Celery('news_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Планировщик периодических задач
app.conf.beat_schedule = {
    'send-test-email-daily': {
        'task': 'news.tasks.send_newsletter',
        'schedule': crontab(hour=2, minute=26),
    },
}
