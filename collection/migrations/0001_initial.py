# Generated by Django 3.0.7 on 2020-07-13 07:54

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(max_length=100)),
                ('publisher_email', models.EmailField(max_length=254, unique=True)),
                ('publisher_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Use the format: +(country) eg +2347000000123', max_length=128, null=True, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('isbn', models.CharField(max_length=25)),
                ('publish_year', models.DateField()),
                ('edition', models.CharField(max_length=100)),
                ('book_format', models.CharField(max_length=100)),
                ('is_available', models.BooleanField()),
                ('language', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Category')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Publisher')),
            ],
        ),
    ]
