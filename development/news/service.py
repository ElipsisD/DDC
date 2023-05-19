import os
from datetime import date

from django.core.mail import send_mail
from constance import config

from news.models import Post


def send_news():
    """Отправка сообщения в соответствии с CONSTANCE"""
    send_mail(
        config.MESSAGE_SUBJECT,
        get_message_text(),
        os.environ.get('EMAIL_ADDRESS'),
        config.DESTINATION_LIST.split(),
        fail_silently=False,
    )


def get_message_text() -> str:
    """Собирает текст сообщения из списка статей новостей за сегодня"""
    today = date.today()
    queryset = Post.objects.filter(publication_date__date=today)
    head = config.MESSAGE_TEXT
    body = '\n'.join(post.title.upper() for post in queryset)
    return head + ' ' + body
