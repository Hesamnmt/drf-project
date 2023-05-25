from django.urls import path
from .views import ArticleList, ArticleDetail , UserList, UserDetail
from rest_framework_simplejwt import views as jwt_views


app_name = 'api'

urlpatterns = [
    path('', ArticleList.as_view(), name='list'),
    path('<int:pk>/', ArticleDetail.as_view(), name='detail'),
    path('user/', UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
