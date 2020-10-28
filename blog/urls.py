from django.urls import path
from .views import PostListView, PostDetailView

#app level urls in blog/

urlpatterns = [   
path('', PostListView.as_view(), name='post_list'),
path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]