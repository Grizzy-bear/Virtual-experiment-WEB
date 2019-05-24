from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def index(request):
    return HttpResponse('hello, welcome to the frontlogin!!!!')


def login(request):
    # 彩蛋
    words = [
        '合抱之木，生于毫末；九层之台，起于累土。',
        '图难于其易，为大于其细。',
        '企者不立，跨者不行。',
        '重为轻根，静为躁君。是以君子终日行不离辎重。',
        '天下难事必作于易，天下大事必作于细。是以圣人终不自为大，故能成其大。',
        '见小曰明，守柔曰强。',
        '道常无名，朴，虽小，天下莫能臣。',
        '上士闻道，勤而行之；中士闻道，若存若亡；下士闻道，大笑之。不笑不足以为道。'
    ]

    word = random.choice(words)
    context = {}
    context['hello'] = word
    return render(request, 'login/index.html',context)
