from django.shortcuts import render
from django.http import HttpResponse
import os,time
from django.conf import settings
from django.core.cache import cache

# Create your views here.


def index(request):
    return HttpResponse('hello welcome to the backweb')


def back(request):
    return render(request, 'backend/index.html')


def back_table(request):
    return render(request, 'backend/table-basic.html')


def redirect_frontlogin(request):
    print("goodsssss!!!")


def pages_blank(request):
    return render(request, 'backend/pages-blank.html')


def icon_fontawesome(request):
    return render(request, 'backend/icon-fontawesome.html')


def back_dealdata(request):
    file_dir = os.path.dirname(os.path.dirname(__file__))
    file_obj = request.FILES.get('file') 
    if file_obj:   # 处理附件上传到方法
        request_set = {}
        print('file--obj', file_obj)
        accessory_dir = file_dir + '/source/'
        print(accessory_dir)
        if not os.path.isdir(accessory_dir):
            os.mkdir(accessory_dir)
        upload_file = "%s/%s" % (accessory_dir, file_obj.name)
        recv_size = 0
        with open(upload_file, 'wb') as new_file:
            for chunk in file_obj.chunks():
                new_file.write(chunk)
        order_id = time.strftime("%Y%m%d%H%M%S",time.localtime())
        cache.set(order_id,upload_file)
        print("ok")
        return HttpResponse(order_id)
    # if request.method == 'POST':
    #     print("kokokoko")
    #     content = request.POST
    #     print(content)
        # print(type(content))
    # else:
    #     print("wrong all!!!!")
    return HttpResponse("ok, hello ")
