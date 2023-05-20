CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True

CONSTANCE_CONFIG = {
    'DESTINATION_LIST': ('mail@mail.ru', 'Список адресатов'),
    'MESSAGE_SUBJECT': ('Новостная рассылка', 'Тема сообщения'),
    'MESSAGE_TEXT': ('Сегодня для вас следующие новости:', 'Тест сообщения'),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'Почтовый клиент': ('DESTINATION_LIST', 'MESSAGE_SUBJECT', 'MESSAGE_TEXT'),
}
