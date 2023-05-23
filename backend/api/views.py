from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from blog.models import Article
from .serializers import ArticleSerializers, UserSerializers
from django.contrib.auth.models import User

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    
    
class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    
    
class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
