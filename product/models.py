from django.db import models
from user.models import User

class Brand(models.Model):
    name         = models.CharField(max_length = 50)
    small_image  = models.CharField(max_length = 2000)

    class Meta:
        db_table = 'brands'

class FirstCategory(models.Model):
    name    = models.CharField(max_length = 50)
    brand   = models.ForeignKey('Brand', on_delete=models.SET_NULL, null = True)

    class Meta:
        db_table = 'firstcategories'


class SecondCategory(models.Model):
    name          = models.CharField(max_length=50)
    firstcategory = models.ForeignKey('FirstCategory', on_delete = models.SET_NULL, null = True)
    brand         = models.ForeignKey('Brand', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'secondcategories'

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
    brand           = models.ForeignKey('Brand', on_delete = models.SET_NULL, null = True)
    firstcategory   = models.ForeignKey('FirstCategory', on_delete=models.SET_NULL, null=True)
    secondcategory  = models.ForeignKey('SecondCategory', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'products'

class UserScore(models.Model):
    user    = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    product = models.ForeignKey('Product', on_delete = models.SET_NULL, null = True)
    score   = models.OneToOneField('Score', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'userscores'

class Score(models.Model):
    half       = models.IntegerField()
    one        = models.IntegerField()
    one_half   = models.IntegerField()
    two        = models.IntegerField()
    two_half   = models.IntegerField()
    three      = models.IntegerField()
    three_half = models.IntegerField()
    four       = models.IntegerField()
    four_half  = models.IntegerField()
    five       = models.IntegerField()

    class Meta:
        db_table = 'scores'
