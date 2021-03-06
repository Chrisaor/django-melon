from django.db import models

from album.models import Album
from artist.models import Artist


class Song(models.Model):
    melon_id = models.CharField('멜론 Song ID', max_length=20, blank=True, null=True, unique=True)
    album = models.ForeignKey(
        Album,
        verbose_name='앨범',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    artists = models.ManyToManyField(
        Artist,
        verbose_name='아티스트 목록',
        blank=True,
    )
    title = models.CharField(
        '곡 제목',
        max_length=100,
    )
    genre = models.CharField(
        '장르',
        max_length=100,
    )
    lyrics = models.TextField(
        '가사',
        blank=True,
    )

    @property
    def release_date(self):
        # self.album의 release_date를 리턴
        return self.album.release_date

    @property
    def formatted_release_date(self):
        return self.release_date.strftime('%Y.%m.%d')

    def __str__(self):
        # 가수명 - 곡제목 (앨범명)
        # TWICE(트와이스) - Heart Shaker (Merry & Happy)
        # 휘성, 김태우 - 호호호빵 (호호호빵)
        #  artists는 self.album의 속성
        if self.album:
            return '{artists} - {title} ({album})'.format(
                artists=', '.join(self.album.artists.values_list('name', flat=True)),
                title=self.title,
                album=self.album.title,
            )
        return self.title