from rest_framework.pagination import BasePaginationSerializer, NextPageField
from rest_framework.templatetags.rest_framework import replace_query_param


class NextTimestampField(NextPageField):
    page_field = 'next'

    def to_representation(self, value):
        if not value.has_next():
            return None

        page = value.next_page_timestamp()
        request = self.context.get('request')
        url = request and request.build_absolute_uri() or ''

        return replace_query_param(url, self.page_field, page)


class NextMaxTimestamp(NextPageField):
    page_field = 'next_max_timestamp'

    def to_representation(self, value):
        if not value.has_next():
            return None

        return value.next_page_timestamp()


class TimestampPaginationSerializer(BasePaginationSerializer):
    """
    Pagination serializer to work with TimestampPaginator
    """
    next = NextTimestampField(source='*')
    next_max_timestamp = NextTimestampField(source='*')