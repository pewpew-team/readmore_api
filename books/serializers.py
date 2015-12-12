from rest_framework import serializers

from books.models import Book
from readmore_api.settings import SITE_URL


class BookSerializer(serializers.ModelSerializer):
    source_url = serializers.SerializerMethodField()

    def get_source_url(self, obj):
        return 'http://{}/{}'.format(SITE_URL, obj.source)

    class Meta:
        model = Book
        fields = ('title', 'description', 'pages_amount', 'user', 'source_url')
