from django.shortcuts import render
from Blog.models import *
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
import time
# from django.urls import reverse
# Create your views here.
def index(request):
    blog = Atlas.objects.all()
    return render(request, "index.html",{'blog': blog})


def blog(request):
    blog = Blog.objects.all()
    return render(request, "blog.html", {'blog': blog})


def blogdetails(request,id):
    article = Blog.objects.filter(id=id)[0]
    return render(request, "blogdetails.html",{'article':article})

def atlas(requist):
    blog = Atlas.objects.all()
    return render(requist,'atlas.html', {'blog': blog})

def written(request):
    # print(os.listdir('./media/upload'))
    return render(request, "written.html")

#被调用的上传的方法
def uploadIme(request,type):  # 上传文件
    if type == 1:
        randomNum = random.randint(0, 9999999999999)
        fileRename = request.FILES.get('img')
        fileRename.name = "%s.jpg" % (randomNum)
        fileRenameName = fileRename.name
        if request.method == 'POST':
            new_img = Blog(
                img=request.FILES.get('img'),
                title=request.POST['title'],
                updatetime=request.POST['updatetime'],
                content=request.POST['content'],
                excerpt=request.POST['excerpt'],
                imageadress='./media/upload/%s' % (fileRenameName)
            )
            new_img.save()
            return fileRenameName
    elif type == 0:
        randomNum = random.randint(0, 9999999999999)
        fileRename = request.FILES.getlist('img')
        print(fileRename)
        for i in fileRename:
            i.name = "%s.jpg" % (randomNum)
#时间转换
        time_now = int(time.time())
        # 转换成localtime
        time_local = time.localtime(time_now)
        # 转换成新的时间格式(2016-05-09 18:59:20)
        dt = time.strftime("%Y-%m-%d", time_local)
        if request.method == 'POST':
            for img in fileRename:
                new_img = Atlas(
                    img=img,
                    updatetime=dt,
                    imageadress='./media/upload/%s' % (img.name)
                )
                new_img.save()

# 新建文章方法
def create(request):
    type = 1
    fileRenameName = uploadIme(request,type)
    return redirect('blog')

#上传方法
def uploadatlas(request):
    type = 0
    fileRenameName = uploadIme(request,type)
    return redirect('atlas')
#上传相册页面
def uploadAtlasPage(request):
    return render(request,'uploadimg.html')
