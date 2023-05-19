import os

from celery import Celery
from celery.schedules import crontab
from constance import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'development.settings')

app = Celery('development')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every-day': {
        'task': 'news.tasks.do_send_news',
        'schedule': crontab(
            minute=config.DISPATCH_TIME.minute,
            hour=config.DISPATCH_TIME.hour,
        ),
    },
}
