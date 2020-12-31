from rest_framework import pagination

# class BuildAPIPagination(pagination.PageNumberPagination):
#     page_size = 5

class BuildAPIPagination(pagination.LimitOffsetPagination):
    # page_size = 5
    max_limit = 5
    default_limit = 5
    # limit_query_param = "lim"