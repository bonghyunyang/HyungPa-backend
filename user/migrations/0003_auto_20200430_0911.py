# Generated by Django 3.0.5 on 2020-04-30 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200428_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activity_index',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='follower_username',
            field=models.ManyToManyField(null=True, through='user.FollowerUser', to='user.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='selected_agreement',
            field=models.BooleanField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_skinproblem',
            field=models.ManyToManyField(null=True, through='user.UserSkinProblem', to='user.SkinProblem'),
        ),
    ]