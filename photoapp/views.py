from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from mainapp.models import Sido, City, Image
from django.core.paginator import Paginator
from django.templatetags.static import static


def photo(request, id, like=3):
    try :
        page = request.GET.get('Image.id',id)
        imageList = Image.objects.all()
        paginator = Paginator(imageList,1)
        imageListpage = paginator.get_page(page)
        imgDetail = Image.objects.get(id=id)
        context = { "imageList": imageListpage, "imgDetail": imgDetail }
        if like == 0:
            imgLike = Image.objects.get(id=id)
            imgLike.image_like += 1
            imgLike.save()
            context = { "imageList": imageListpage, "imgDetail": imgDetail, "imgLike.image_like": imgLike.image_like }
        elif like == 1:
            imgDislike = Image.objects.get(id=id)
            imgDislike.image_dislike += 1
            imgDislike.save()
            context = { "imageList": imageListpage, "imgDetail": imgDetail, "imgDislike.image_dislike": imgDislike.image_dislike }


    except Image.DoesNotExist:
        context = { "msg" : "게시물이 존재하지 않습니다." }

    return render(request, "photo.html", context)