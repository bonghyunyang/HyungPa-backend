from django.db import models

class User(models.Model):
    email              = models.CharField(max_length = 50)
    password           = models.CharField(max_length = 200)
    birth_date         = models.DateField()
    phone_number       = models.CharField(max_length = 20)
    created_at         = models.DateTimeField(auto_now_add = True)
    updated_at         = models.DateTimeField(auto_now_add = True)
    nickname           = models.CharField(max_length = 50)
    self_introduction  = models.CharField(max_length = 200)
    profile_image      = models.URLField(max_length = 2000)
    activity_index     = models.IntegerField(default = 0)
    selected_agreement = models.BooleanField(default = 1)
    skintype           = models.ForeignKey('SkinType', on_delete = models.SET_NULL, null = True)
    skintone           = models.ForeignKey('SkinTone', on_delete = models.SET_NULL, null = True)
    user_skinproblem   = models.ManyToManyField('SkinProblem', through = 'UserSkinProblem')
    follower_username  = models.ManyToManyField('self', symmetrical = False, through = 'FollowerUser')

    class Meta:
        db_table = 'users'

class SkinType(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'skintypes'

class SkinTone(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'skintones'

class SkinProblem(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'skinproblems'

class UserSkinProblem(models.Model):
    user         = models.ForeignKey('User', on_delete = models.SET_NULL, null = True)
    skinproblem = models.ForeignKey('SkinProblem', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'user_skinproblems'

class FollowerUser(models.Model):
    user         = models.ForeignKey('User', on_delete = models.SET_NULL,null = True)
    follower     = models.ForeignKey('User', related_name = 'follower', on_delete = models.SET_NULL, null = True)
    published_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'follower_users'