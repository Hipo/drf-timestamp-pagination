from rest_framework.pagination import BasePaginationSerializer, NextPageField
from rest_framework.templatetags.rest_framework import replace_query_param
from rest_framework.settings import api_settings


class NextTimestampField(NextPageField):
    page_field = 'next'

    def to_representation(self, value):
        if not value.has_next():
            return None

        page = value.next_page_timestamp()
        request = self.context.get('request')

        use_absolute_url = getattr(api_settings, 'PAGINATION_USE_ABSOLUTE_URL', None)
        url = use_absolute_url and request and request.build_absolute_uri() or ''

        return replace_query_param(url, self.page_field, page)


class TimestampPaginationSerializer(BasePaginationSerializer):
    """

    """
    next = NextTimestampField(source='*')