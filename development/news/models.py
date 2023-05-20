from django.contrib.auth.models import User
from django.db import models
from versatileimagefield.fields import VersatileImageField


def get_user():
    return User.objects.get(id=1)


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='заголовок')
    body = models.TextField(verbose_name='текст')
    image = VersatileImageField(verbose_name='изображение', upload_to='media/', blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='автор', default=get_user)
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
