# Generated by Django 2.0.2 on 2018-02-08 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='앨범명')),
                ('img_cover', models.ImageField(blank=True, upload_to='album', verbose_name='커버 이미지')),
                ('release_date', models.DateField()),
                ('artists', models.ManyToManyField(to='artist.Artist', verbose_name='아티스트 목록')),
            ],
        ),
    ]
