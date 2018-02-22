from django.shortcuts import redirect

from crawler.song import SongData
from song.models import Song

__all__ = (
    'song_add_from_melon',
)

def song_add_from_melon(request):
    if request.method == 'POST':
        song_id = request.POST['song_id']
        song = SongData(song_id)
        song.get_detail()
        print(song.artist_id)
        print(song.album_id)

        # song detail페이지에 있는 Artist ID를 사용해서
        # Artist 정보를 저장( 없으면 생성, 있으면 업데이트)
        # artist = ArtistData(song.artist_id)

        # title = song.title
        # genre = song.genre
        # lyrics = song.lyrics

        song, _ = Song.objects.update_or_create(
            melon_id=song_id,
            defaults={
                'title': song.title,
                'genre': song.genre,
                'lyrics': song.lyrics,
            }
        )
        return redirect('song:song-list')