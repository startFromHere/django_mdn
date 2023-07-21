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

from django.http import HttpResponseRedirect

class CommentList(generic.ListView):
    model = Comment

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(blog_id__exact=pk)
    
    def form_valid(self, form):
        qs = Comment.objects.filter(pk__in=list(map(int, self.request.POST.getlist('checkboxes'))))
        qs.delete()

        return super(CommentCreate, self).form_valid(form)
    
    def get_success_url(self) -> str:
        blog = get_object_or_404(Blog, pk = self.kwargs['pk']) 
        return blog.get_absolute_url()

class CommentsManage(generic.ListView):
    model = Comment
    template_name = 'blog/comment_manage.html'

    def get_queryset(self):
        pk = self.kwargs['pk']
        self.comments = Comment.objects.filter(blog_id__exact=pk)
        return self.comments
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # pk = self.kwargs['pk']
        # comments = Comment.objects.filter(blog_id__exact=pk)
        context['comments'] = self.comments
        context['blog_name'] = list(self.comments)[0].blog.title
        return context
    
    # def form_valid(self, form):
    #     qs = Comment.objects.filter(pk__in=list(map(int, self.request.POST.getlist('checkboxes'))))
    #     qs.delete()

    #     return super(CommentCreate, self).form_valid(form)
    
    def get_success_url(self) -> str:
        blog = get_object_or_404(Blog, pk = self.kwargs['pk']) 
        return blog.get_absolute_url()
    
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """

        qs = Comment.objects.filter(id__in=list(map(int, self.request.POST.getlist('comment_id'))))
        qs.delete()
        return HttpResponseRedirect(self.get_success_url())

    