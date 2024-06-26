# Generated by Django 4.2.7 on 2024-04-21 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('TECH', 'Technology'), ('ART', 'Art'), ('FOOD', 'Food'), ('TRAVEL', 'Travel'), ('OTHER', 'Other')], default='OTHER', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
