from rest_framework.pagination import BasePaginationSerializer, NextPageField, PreviousPageField
from rest_framework.templatetags.rest_framework import replace_query_param


class MaxTimestampField(PreviousPageField):
    page_field = 'max_timestamp'
    #TODO: add flag for absolute uri (inject to DRF settings)

    def to_representation(self, value):
        if not value.has_next():
            return None
        page = value.next_page_number()
        request = self.context.get('request')
        url = request and request.build_absolute_uri() or ''
        return replace_query_param(url, self.page_field, page)


class MinTimestampField(NextPageField):
    page_field = 'min_timestamp'


class TimestampPaginationSerializer(BasePaginationSerializer):
    """

    """
    min_timestamp = MinTimestampField(source='*')
    max_timestamp = MaxTimestampField(source='*')