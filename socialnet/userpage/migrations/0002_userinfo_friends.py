# Generated by Django 4.0.2 on 2022-02-25 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='friends',
            field=models.ManyToManyField(to='userpage.UserInfo'),
        ),
    ]
