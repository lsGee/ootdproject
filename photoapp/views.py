from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from mainapp.models import Sido, City, Image
from django.core.paginator import Paginator
from django.templatetags.static import static
from datetime import date


def photo(request, list, like=3):
    city = int(request.GET['city'][:5])
    id = request.GET['id']
    sort = request.GET['sort']
    data = request.GET['data']
    # like = request.GET['image_like']
    # dislike = request.GET['image_dislike']
    today = date.today()
    # imgDetail = Image.objects.get(id=id)
    if data == "all":
        try:
            if sort != "":
                imageList = Image.objects.filter(city_id_id=city).order_by(sort).reverse()
            else:
                imageList = Image.objects.filter(city_id_id=city).order_by('image_date').reverse()
            print(imageList)
            imgDetail = imageList[list]
            if like == 3:
                imgDetail.image_cnt += 1;
                imgDetail.save()
            # id = imgDetail.id
            page = request.GET.get('page', list + 1)
            print(imgDetail)
            paginator = Paginator(imageList, 1)
            imageListpage = paginator.get_page(page)
            print(imageListpage)
            print(imageListpage.number)
            context = {"imageList": imageListpage, "imgDetail": imgDetail, "sort": sort, "data": data}

            if request.method == "POST":
                if like == 0:
                    imgLike = Image.objects.get(id=id)
                    imgLike.image_like += 1
                    imgLike.save()
                    context = {"imageList": imageListpage, "imgDetail": imgDetail,
                               "imgLike.image_like": imgLike.image_like, "sort": sort, "data": data}
                elif like == 1:
                    imgDislike = Image.objects.get(id=id)
                    imgDislike.image_dislike += 1
                    imgDislike.save()
                    context = {"imageList": imageListpage, "imgDetail": imgDetail,
                               "imgDislike.image_dislike": imgDislike.image_dislike, "sort": sort, "data": data}
        except Image.DoesNotExist:
            context = {"msg": "게시물이 존재하지 않습니다."}

        return render(request, "photo.html", context)

    else :
        try :
            if sort !="" :
                imageList = Image.objects.filter(city_id_id= city,
                                                 image_date__month=today.month,
                                                 image_date__day=today.day).order_by(sort).reverse()
            else:
                imageList = Image.objects.filter(city_id_id=city,
                                                 image_date__month=today.month,
                                                 image_date__day=today.day).order_by('image_date').reverse()
            print(imageList)
            imgDetail = imageList[list]
            if like == 3 :
                imgDetail.image_cnt += 1;
                imgDetail.save()
            # id = imgDetail.id
            page = request.GET.get('page',list+1)
            print(imgDetail)
            paginator = Paginator(imageList,1)
            imageListpage = paginator.get_page(page)
            print(imageListpage)
            print(imageListpage.number)
            context = { "imageList": imageListpage, "imgDetail": imgDetail, "sort": sort }

            if request.method == "POST" :
                if like == 0:
                    imgLike = Image.objects.get(id=id)
                    imgLike.image_like += 1
                    imgLike.save()
                    context = { "imageList": imageListpage, "imgDetail": imgDetail, "imgLike.image_like": imgLike.image_like, "sort": sort }
                elif like == 1:
                    imgDislike = Image.objects.get(id=id)
                    imgDislike.image_dislike += 1
                    imgDislike.save()
                    context = { "imageList": imageListpage, "imgDetail": imgDetail, "imgDislike.image_dislike": imgDislike.image_dislike, "sort": sort }


        except Image.DoesNotExist :
            context = { "msg" : "게시물이 존재하지 않습니다." }

        return render(request, "photo.html", context)