

class TimestampPaginationMixin(object):
    timestamp_field = None
    next_timestamp_kwarg = 'next'

    def paginate_queryset(self, queryset):
        """
        Paginate a queryset if required, either returning a page object,
        or `None` if pagination is not configured for this view.
        """
        page_size = self.get_paginate_by()
        if not page_size:
            return None

        assert self.timestamp_field is not None, '`timestamp_field` must be specified for TimestampPaginator to paginate'

        paginator = self.paginator_class(queryset, 'timestamp', page_size)

        next_timestamp_kwarg = self.kwargs.get(self.next_timestamp_kwarg)
        next_timestamp_query_param = self.request.query_params.get(self.next_timestamp_kwarg)
        next_timestamp = next_timestamp_kwarg or next_timestamp_query_param

        return paginator.page(timestamp=next_timestamp)
