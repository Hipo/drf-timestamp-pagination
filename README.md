# DRF Timestamp Pagination
A paginator class for [Django Rest Framework](https://github.com/tomchristie/django-rest-framework) that uses [Timestamp Paginator](https://github.com/hipo/django-timestamp-paginator)

## Why we needed this?

Classical pagination (?page=2) doesn't work properly with actively updated list pages.

#### Example:
Imagine a web page where people upload their pet's pictures. 
 - Anyone can upload a picture anytime and it will be listed. 
 - The newest picture appears at the top of the page. 
 - When the list will be complete, the users will go to the second page (by a link or infinite loader). 

This will work fine.

However, if during this time period, a new image will be uploaded, 
the last image of the first page will become the first item of the second page.

In order to prevent this problem, there are many alternative ways that can be used. 
One of the best alternatives is to use timestamps instead of page numbers.

This paginator makes the pagination by the timestamps of the items. 

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
    "next": "https://api.example.com/feed/?next=1425028897.60",
    "next_max_timestamp" : 1425028897.60,
    "results": [
        { result set }
    ]
}
```
