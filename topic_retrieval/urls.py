from django.urls import path

from . import views

#url_namespace
app_name = 'topic_retrieval'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search', views.SearchView.as_view(), name='search'),
    path('tweets', views.TweetsView.as_view(), name='tweets'),
    path('update_tweets',views.update_latest_tweets, name = 'update_tweets')
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
   
    
]