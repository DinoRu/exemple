# Generated by Django 4.1.5 on 2023-01-21 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_subscribe_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribeUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Subscribe',
        ),
    ]