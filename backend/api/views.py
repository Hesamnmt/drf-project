from rest_framework.generics import ListAPIView
from blog.models import Article
from .serializers import ArticleSerializers


class ArticleList(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers