from django.contrib import admin
from django.utils.safestring import mark_safe
from django_summernote.admin import SummernoteModelAdmin

from .models import Post


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ('title', 'author', 'get_html_photo', 'publication_date')
    fields = ('title', 'body', 'author', 'get_html_photo', 'image', 'publication_date')
    readonly_fields = ('get_html_photo', 'publication_date')
    save_on_top = True

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f'<img src={object.image.url} width=50>')

    get_html_photo.short_description = 'изображение'


admin.site.register(Post, PostAdmin)
