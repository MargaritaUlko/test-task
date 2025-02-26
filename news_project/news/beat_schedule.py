# from celery.schedules import crontab
# from .tasks import send_news_email
# from celery import Celery

# app = Celery('news_project')

# app.conf.beat_schedule = {
#     'check-news-send-time-every-minute': {
#         'task': 'news.tasks.send_news_email',
#         'schedule': crontab(minute='*'),  # Проверяем каждую минуту
#     },
# }

# app.conf.timezone = 'Asia/Krasnoyarsk'
