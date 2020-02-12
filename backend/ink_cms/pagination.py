from rest_framework import pagination


class InkPagination(pagination.PageNumberPagination):
    page_size = 10
