from django.urls import path
from . import views
from .views import ArticleAPIView,article_detail,article_list, ArticleDetails, RegisterView, ShowUser, log_in, GenericAPIView
urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    #path('article/', views.article_list,name='article_list'),
    path('details/<int:id>/',ArticleDetails.as_view()),
    #path('details/<int:pk>/',article_detail)
    path('genericarticle/<int:id>/',GenericAPIView.as_view()),
    path('register/',RegisterView),
    path('allusers/',ShowUser),
    path('login/',log_in)
]