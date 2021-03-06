# Generated by Django 3.2.6 on 2021-08-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=250, verbose_name='titre')),
                ('image', models.FileField(upload_to='Blog_img')),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
