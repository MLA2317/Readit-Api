from rest_framework import serializers
from ..models import Article, Tag, Category, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class ArticleGetSerializer(serializers.ModelSerializer):
    # category_name = serializers.CharField(source='category.title', read_only=True) # 1chi uslub
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'image', 'category', 'tags', 'description', 'created_date']


class ArticlePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'image', 'category', 'tags', 'description', 'created_date']

    def create(self, validated_data):
        requests = self.context.get('request')
        author = requests.user.profile
        instance = super().create(validated_data)
        print(validated_data)
        instance.author = author
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'article', 'description', 'created_date']
        extra_kwargs = {
            'article': {'required': False}
        }

    def create(self, validated_data):
        request = self.context['request']
        article_id = self.context['article_id']
        author_id = request.user.profile.id
        description = validated_data.get('description')
        instance = Comment.objects.create(article_id=article_id, author_id=author_id, description=description)
        return instance
