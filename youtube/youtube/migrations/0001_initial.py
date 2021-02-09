# Generated by Django 3.1.5 on 2021-02-09 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='videoTbl',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('video_url', models.CharField(max_length=64)),
                ('image_url', models.CharField(max_length=64)),
                ('upload_time', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='playlistTbl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(default='재생목록', max_length=16)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='playlistItemTbl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube.playlisttbl')),
                ('videoid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube.videotbl')),
            ],
        ),
        migrations.CreateModel(
            name='historyTbl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('videoid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtube.videotbl')),
            ],
        ),
    ]
