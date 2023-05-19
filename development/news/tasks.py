# from constance import config
# from django_celery_beat.models import CrontabSchedule, PeriodicTask

from celery_app import app
from news.service import send_news


@app.task(bind=True, max_retries=3)
def do_send_news(self):
    """Отправка сообщения в соответствии с CONSTANCE"""
    try:
        send_news()
    except Exception as err:
        self.retry(exc=err, countdown=10)


# schedule = CrontabSchedule(minute=config.DISPATCH_TIME.minute, hour=config.DISPATCH_TIME.hour)
# if task := PeriodicTask.objects.get(name='Ежедневные новости'):
#     print(schedule, task)
#     if task.crontab != schedule:
#         schedule.save()
#         task.crontab.delete()
#         PeriodicTask.objects.update(crontab=schedule)
# else:
#     print(schedule, 123)
#     schedule.save()
#     PeriodicTask.objects.update_or_create(crontab=schedule, name='Ежедневные новости',
#                                           task='news.tasks.do_send_news')
