# DRF Timestamp Pagination
DRF Pagination to work with [Timestamp Paginator](https://github.com/umutbozkurt/django-timestamp-paginator)

## Installation
`pip install drf-timestamp-pagination`

## Usage
```python
from django_timestamp_paginator import TimestampPaginator
from drf_timestamp_pagination import TimestampPaginationSerializer, TimestampPaginationMixin


class CommentsView(TimestampPaginationMixin, ListCreateAPIView):  # Add mixin to left-hand side
	pagination_serializer_class = TimestampPaginationSerializer
	paginator_class = TimestampPaginator
	timestamp_field = 'timestamp'

### Rest of the class
```

Done.
`paginate_by`, `paginate_by_param`, `max_paginate_by` also applies to TimestampPaginationSerializer.

## Sample View Response

```
{
    "next": "?next=1425028897.60",
    "results": [
        { result set }
    ]
}
```

------------------------
Special Thanks to @yigitguler and whole @Hipo team for inspiration and contributions.

![Hipo](https://avatars1.githubusercontent.com/u/1497148?v=3&s=50)
