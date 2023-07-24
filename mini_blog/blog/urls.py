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
    path('<int:pk>/edit', views.BlogEditView.as_view(), name='blog_edit', kwargs={'slug': None}),
]

urlpatterns += [
    path('<int:pk>/comment/create', views.CommentCreate.as_view(), name='comment_create'),
]

urlpatterns += [
    path('blog/<int:pk>/comment/manage', views.CommentsManage.as_view(), name='comments_manage'),
]
