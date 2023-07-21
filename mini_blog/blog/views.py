from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Blogger, Blog, Comment
from django.contrib.auth.models import User


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

# @login_required
# @permission_required('catalog.can_add_comment', raise_exception=True)
# def add_comment_to_blog(request, pk):


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
# from models import Blog

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']

    # def get_initial(self) -> Dict[str, Any]:
    #     info = super().get_initial()
    #     info['user_name'] = self.request.user.username
    #     info['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk']) 
    #     return info

    # def get_context_data(self, **kwargs):
    #     context = super(CommentCreate, self).get_context_data(**kwargs)
    #     context["blog"] = get_object_or_404(Blog, pk = self.kwargs['pk']) 
    #     context["user_name"] = self.request.user.username
    #     return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user_name = self.request.user.username
        form.instance.blog = get_object_or_404(Blog, pk = self.kwargs['pk']) 

        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self) -> str:
        blog = get_object_or_404(Blog, pk = self.kwargs['pk']) 
        return blog.get_absolute_url()
