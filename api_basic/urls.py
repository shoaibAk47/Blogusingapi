from django.urls import path,include
from . import views
from .views import ArticleAPIView,article_detail,article_list, ArticleDetails, RegisterView, ShowUser
urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    #path('article/', views.article_list,name='article_list'),
    path('details/<int:id>/',ArticleDetails.as_view()),
    #path('details/<int:pk>/',article_detail)
    #path('genericarticle/<int:id>/',GenericAPIView.as_view()),
    path('register/',RegisterView),
    path('allusers/',ShowUser),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]