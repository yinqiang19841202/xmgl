# Generated by Django 3.0.3 on 2020-03-01 08:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Xmgl',
            fields=[
                ('xmbh', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('xmmc', models.CharField(max_length=256, unique=True)),
                ('xmjl', models.CharField(max_length=32)),
                ('xmlxdh', models.CharField(max_length=32)),
                ('bz', models.CharField(max_length=500)),
                ('c_tmie', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '项目管理',
                'verbose_name_plural': '项目管理',
            },
        ),
    ]
