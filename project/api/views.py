from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializer import ArticleGetSerializer, ArticlePostSerializer, CategorySerializer, TagSerializer, CommentSerializer
from ..models import Category, Tag, Article, Comment
from .permissions import IsAdminUserOrReadOnly, IsAuthenticatedOrReadOnly


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.order_by('-id')
    # serializer_class = ArticlePostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# 1 uslub
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGetSerializer
        if self.request.method == 'POST':
            return ArticlePostSerializer
        return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# 2 uslub
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     override_serializer = ArticlePostSerializer(serializer.data)
    #     return Response(override_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BlogRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGetSerializer
        return ArticlePostSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/api/blog/article/{article_id}/comment-list-create/
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permissions = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        article_id = self.kwargs.get('article_id')
        if article_id:
            qs = qs.filter(article_id=article_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['article_id'] = self.kwargs.get('article_id')
        return ctx

