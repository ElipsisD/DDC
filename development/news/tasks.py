from celery_app import app
from news.service import send_news


@app.task(bind=True, max_retries=3)
def do_send_news(self) -> None:
    """Отправка сообщения в соответствии с CONSTANCE"""
    try:
        send_news()
    except Exception as err:
        self.retry(exc=err, countdown=10)
