from django.urls import path
from .views import CategoryListCreateAPIView, CategoryRUDAPIView, TagListCreateAPIView, \
    TagRUDAPIView, BlogListCreateAPIView, BlogRUDAPIView, CommentListCreateAPIView


urlpatterns = [
    path('category-list/', CategoryListCreateAPIView.as_view()),
    path('category-rud/<int:pk>/', CategoryRUDAPIView.as_view()),
    path('tag-list/', TagListCreateAPIView.as_view()),
    path('tag-rud/<int:pk>/', TagRUDAPIView.as_view()),

    path('blog-list-create/', BlogListCreateAPIView.as_view()),
    path('blog-rud/<int:pk>/', BlogRUDAPIView.as_view()),

    path('article/<int:article_id>/comment-list-create/', CommentListCreateAPIView.as_view())
]
