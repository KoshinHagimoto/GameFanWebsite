import random

from django.shortcuts import get_object_or_404, render

from .models import Player

def index(request):
    img_urls = ['https://publicdomainq.net/images/201806/16s/publicdomainq-0023181ohc.jpg', 'https://www.pakutaso.com/shared/img/thumb/TSU93_kinpakusc_TP_V.jpg', 'https://www.pakutaso.com/shared/img/thumb/TSU88_scss01_TP_V.jpg']
    img_url = random.choice(img_urls)
    context = {'img_url':img_url}
    return render(request, 'sports/index.html', context)

def rules(request):
    return render(request, 'sports/rules.html')

def notables(request):
    player_list = Player.objects.all()
    return render(request, 'sports/notables.html', {'player_list':player_list})

def detail(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    return render(request, 'sports/detail.html', {'player':player})

def external(request):
    urlLists = ['https://www.soccer-king.jp/', 'https://web.gekisaka.jp/']
    return render(request, 'sports/external.html', {'urlLists':urlLists})

