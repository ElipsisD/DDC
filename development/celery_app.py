import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'development.settings')

app = Celery('development')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'Mail': {
        'task': 'news.tasks.do_send_news',
        'schedule': crontab(
            minute=0,
            hour=11,
        ),
    },
    'Weather': {
        'task': 'places.tasks.do_get_weather',
        'schedule': crontab(
            minute=0
        )
    }
}
