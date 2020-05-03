from django.db import models
from user.models import User
from product.models import Product

class Review(models.Model):
    description  = models.TextField()
    like_number  = models.IntegerField()
    published_at = models.DateTimeField(auto_now_add = True)
    updated_at   = models.DateTimeField(auto_now = True)
    view_number  = models.IntegerField()
    user         = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    product      = models.ForeignKey(Product, on_delete=models.SET_NULL, null = True)

    class Meta:
        db_table = 'reviews'

class ReviewComment(models.Model):
    comment           = models.CharField(max_length = 200)
    created_at        = models.DateTimeField(auto_now_add = True)
    user              = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    review            = models.ForeignKey('Review', on_delete = models.SET_NULL, null = True)
    is_original       = models.BooleanField(null=True)
    original_comment  = models.ForeignKey('ReviewComment', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'review_comments'