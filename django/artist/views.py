from django.shortcuts import render, redirect

from .models import Artist


def artist_list(request):
    artists = Artist.objects.all()
    context = {
        'artists': artists,
    }
    return render(
        request,
        'artist/artist_list.html',
        context,
    )

def artist_add(request):
    # HTML에 Artist클래스가 받을 수 있는 모든 input을 구현
    # img_profile은 제외
    # mothod가 POST면 request.POST에서 해당 데이터 처리
    # 새 Artist객체를 만들고 artist_list로 이동
    # method가 GET이면 artist_add.html을 표시
    context = {

    }
    if request.method == 'POST':
        name = request.POST['name']
        # real_name = request.POST['real_name']
        # nationality = request.POST['nationality']
        # birth_date = request.POST['birth_date']
        # constellation = request.POST['constellation']
        # blood_type = request.POST['blood_type']
        # intro = request.POST['intro']

        artist = Artist.objects.create(
            name = name,
        #     real_name = real_name,
        #     nationality = nationality,
        #     birth_date = birth_date,
        #     constellation = constellation,
        #     blood_type = blood_type,
        #     intro = intro,
        )
        return redirect('artist:artist-list')
    else:
        return render(request, 'artist/artist_add.html')