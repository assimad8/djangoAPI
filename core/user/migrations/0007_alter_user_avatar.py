# Generated by Django 4.2.7 on 2024-04-24 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0006_user_posts_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar/default.png', upload_to='avatart/'),
        ),
    ]
