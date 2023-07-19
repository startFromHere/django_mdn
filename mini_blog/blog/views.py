from django.shortcuts import render
from .models import Blogger, Blog, Comment


# Create your views here.
def index(request):
    blogs_num = Blog.objects.all().count()
    bloggers_num = Blogger.objects.all().count()

    context = {
        'blogs_num': blogs_num,
        'bloggers_num': bloggers_num,
    }

    return render(request, 'index.html', context=context)

from django.views import generic

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = Blog

class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 10

class BloggerDetailView(generic.DetailView):
    model = Blogger

class BlogCommentCreate(generic.FormView):
    model = Comment