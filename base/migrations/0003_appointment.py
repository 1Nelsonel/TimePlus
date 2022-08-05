# Generated by Django 4.0.5 on 2022-08-05 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_blog_service_comment_blog_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('ptype', models.CharField(max_length=50)),
                ('bedroom', models.IntegerField()),
                ('frequency', models.IntegerField()),
                ('time', models.TimeField()),
                ('year', models.DateField()),
            ],
        ),
    ]