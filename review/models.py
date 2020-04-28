from django.db import models
from user.models import User
from product.models import Product

class Review(models.Model):
    description  = models.CharField(max_length = 2000)
    like_number  = models.IntegerField()
    published_at = models.DateTimeField(auto_now_add = True)
    updated_at   = models.DateTimeField(auto_now = True)
    view_number  = models.IntegerField()
    user         = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    product      = models.ForeignKey(Product, on_delete=models.SET_NULL, null = True)

    class Meta:
        db_table = 'reviews'

class ReviewComment(models.Model):
    comment        = models.CharField(max_length = 200)
    created_at     = models.DateTimeField(auto_now_add = True)
    user           = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    review         = models.ForeignKey('Review', on_delete = models.SET_NULL, null = True)
    comment_reply  = models.ManyToManyField('self', symmetrical = False, through = 'CommentReply')

    class Meta:
        db_table = 'review_comments'

class CommentReply(models.Model):
    comment         = models.CharField(max_length = 200)
    created_at      = models.DateTimeField(auto_now_add = True)
    user            = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reply           = models.ForeignKey('ReviewComment', related_name='reply', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'comment_replies'