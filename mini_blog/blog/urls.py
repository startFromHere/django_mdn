from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger_detail'),
]

urlpatterns += [
    path('comment/create/<int:pk>', views.CommentCreate.as_view(), name='comment_create'),
]
