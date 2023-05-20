from celery_app import app
from places.service import get_weather


@app.task(bind=True, max_retries=3)
def do_get_weather(self) -> None:
    """Получение сводки о погоде во всех местах"""
    try:
        get_weather()
    except Exception as err:
        self.retry(exc=err, countdown=10)
