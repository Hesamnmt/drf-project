from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from blog.models import Article
from .serializers import ArticleSerializers, UserSerializers
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from .permissions import IsSuperUser, IsStaffOrReadOnly, IsAuthorOrReadOnly

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    
    
class ArticleDetail(RetrieveUpdateDestroyAPIView):        
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = [IsAuthorOrReadOnly, IsStaffOrReadOnly]

 
class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsSuperUser,]    
    
     
class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsSuperUser,]
     