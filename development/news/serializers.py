from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from news.models import Post


class PostSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__200x200'),
        ]
    )

    class Meta:
        model = Post
        fields = '__all__'
