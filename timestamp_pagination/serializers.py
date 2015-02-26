from rest_framework.pagination import BasePaginationSerializer, NextPageField, PreviousPageField
from rest_framework.templatetags.rest_framework import replace_query_param
from rest_framework.settings import api_settings



class MaxTimestampField(PreviousPageField):
    page_field = 'max_timestamp'
    #TODO: add flag for absolute uri (inject to DRF settings)

    def to_representation(self, value):
        if not value.has_next():
            return None

        page = value.next_page_number()
        request = self.context.get('request')

        use_absolute_url = getattr(api_settings, 'PAGINATION_USE_ABSOLUTE_URL', None)
        url = use_absolute_url and request and request.build_absolute_uri() or ''

        return replace_query_param(url, self.page_field, page)


class MinTimestampField(NextPageField):
    page_field = 'min_timestamp'

    def to_representation(self, value):
        if not value.has_previous():
            return None

        page = value.previous_page_number()
        request = self.context.get('request')

        use_absolute_url = getattr(api_settings, 'PAGINATION_USE_ABSOLUTE_URL', None)
        url = use_absolute_url and request and request.build_absolute_uri() or ''

        return replace_query_param(url, self.page_field, page)


class TimestampPaginationSerializer(BasePaginationSerializer):
    """

    """
    min_timestamp = MinTimestampField(source='*')
    max_timestamp = MaxTimestampField(source='*')