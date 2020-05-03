from django.db import models
from user.models import User

class Post(models.Model):
    title        = models.CharField(max_length = 500,default = 'TITLE')
    description  = models.TextField()
    like_number  = models.IntegerField()
    published_at = models.DateTimeField(auto_now_add = True)
    updated_at   = models.DateTimeField(auto_now = True)
    view_number  = models.IntegerField()
    user         = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)

    class Meta:
        db_table = 'posts'

class PostComment(models.Model):
    comment            = models.CharField(max_length = 200)
    created_at         = models.DateTimeField(auto_now_add = True)
    user               = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    review             = models.ForeignKey('Post', on_delete = models.SET_NULL, null = True)
    original_comment  = models.ForeignKey('PostComment', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'post_comments'