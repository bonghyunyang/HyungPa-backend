from django.db import models
from user.models import User

class FirstCategory(models.Model):
    name    = models.CharField(max_length = 50)

    class Meta:
        db_table = 'first_categories'


class SecondCategory(models.Model):
    name          = models.CharField(max_length=50)
    firstcategory = models.ForeignKey('FirstCategory', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'second_categories'

class Product(models.Model):
    name            = models.TextField(max_length = 200)
    price           = models.IntegerField()
    capacity        = models.CharField(max_length = 50)
    product_image   = models.URLField(max_length = 1000)
    like_nums       = models.IntegerField()
    review_nums     = models.IntegerField()
    mini_nums       = models.IntegerField()
    published_at    = models.DateTimeField(auto_now_add = True)
    updated_at      = models.DateTimeField(auto_now_add = True)
    brand_name      = models.CharField(max_length = 100, null = True)
    firstcategory   = models.ForeignKey('FirstCategory', on_delete=models.SET_NULL, null=True)
    secondcategory  = models.ForeignKey('SecondCategory', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'products'

class UserScore(models.Model):
    user    = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    product = models.ForeignKey('Product', on_delete = models.SET_NULL, null = True)
    score   = models.FloatField()

    class Meta:
        db_table = 'user_scores'