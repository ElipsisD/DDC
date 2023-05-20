import os
from datetime import date

from constance import config
from django.core.mail import send_mail

from news.models import Post

msg_template = """
{head}

{body}
"""

def send_news() -> None:
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
    return msg_template.format(body=body, head=head)
