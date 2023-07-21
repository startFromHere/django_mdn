from django.db import models
# from django.contrib.auth.models import User
from datetime import date
import uuid
from django.urls import reverse

# Create your models here.

class Blogger(models.Model):
    name = models.CharField(max_length=100)
    intro = models.TextField(help_text='info of this author')

    def get_absolute_url(self):
        return reverse("blogger_detail", args=[str(self.id)])
    
    def __str__(self) -> str:
        return self.name

class Blog(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this blog')
    title = models.CharField(max_length=200, help_text="Enter the title of this blog")
    content = models.TextField(help_text='blog content')
    create_date = models.DateField(null=True, blank=True)
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["-create_date"]
        permissions = (("can_add_comment", "add a comment"),)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
    
    def get_comment_url(self):
        # return "{% url 'comment_create' %}?pk={{self.pk}}"
        # fixme： 上面的写法可以吗？
        return reverse("comment_create", kwargs={'pk': self.pk})
    

class Comment(models.Model):
    user_name = models.CharField(max_length=200)
    content = models.TextField(help_text='comment content')
    post_date = models.DateField(auto_now_add=True)
    blog = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ["post_date"]

    def __str__(self) -> str:
        return self.user_name + ":" + self.content[:20]