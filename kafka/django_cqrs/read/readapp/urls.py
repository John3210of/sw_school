from django.urls import path
from .views import BookListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # 모든 책 목록 조회
]