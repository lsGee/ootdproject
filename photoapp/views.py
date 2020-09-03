from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from mainapp.models import Sido, City, Image
from django.core.paginator import Paginator
from django.templatetags.static import static
from datetime import date


def photo(request, list):
    city = int(request.GET['city'][:5])
    sort = request.GET['sort']
    data = request.GET['data']
    today = date.today()
    if data == "all":
        try:
            if sort != "":
                alist = Image.objects.filter(city_id=city,
                                             image_date__month=today.month,
                                             image_date__lt=today).order_by(sort).reverse()
            else:
                alist = Image.objects.filter(city_id=city,
                                             image_date__month=today.month,
                                             image_date__lt=today).order_by('image_date').reverse()
            aDetail = alist[list]
            aDetail.image_cnt += 1;
            aDetail.save()
            page = request.GET.get('page', list + 1)
            paginator = Paginator(alist, 1)
            aListpage = paginator.get_page(page)
            context = {"alist": aListpage, "aDetail": aDetail, "sort": sort, "data": data}
        except Image.DoesNotExist:
            context = {"msg": "게시물이 존재하지 않습니다."}

        return render(request, "photo.html", context)

    elif data == "today" :
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


        except Image.DoesNotExist :
            context = { "msg" : "게시물이 존재하지 않습니다." }

        return render(request, "photo.html", context)

    else :
        try:
            if sort != "":
                blist = Image.objects.filter(image_date__month=today.month,
                                             image_date__day=today.day).order_by(sort).reverse()
            else:
                blist = Image.objects.filter(image_date__month=today.month,
                                             image_date__day=today.day).order_by('image_date').reverse()
            bDetail = blist[list]
            bDetail.image_cnt += 1;
            bDetail.save()
            page = request.GET.get('page', list + 1)
            paginator = Paginator(blist, 1)
            bListpage = paginator.get_page(page)
            context = {"blist": bListpage, "bDetail": bDetail, "sort": sort, "data": data}
        except Image.DoesNotExist:
            context = {"msg": "게시물이 존재하지 않습니다."}

        return render(request, "photo.html", context)

def likeCount(request) :
    # if request.method == "POST" :
    id = request.GET.get("id")
    imgDetail = Image.objects.get(id=id)
    imgDetail.image_like += 1
    imgDetail.save()

    jsonContent={ "like": imgDetail.image_like }
    return JsonResponse(jsonContent, json_dumps_params={'ensure_ascii': False})

def dislikeCount(request) :
    # if request.method == "POST" :
    id = request.GET.get("id")
    imgDetail = Image.objects.get(id=id)
    imgDetail.image_dislike += 1
    imgDetail.save()

    jsonContent={ "dislike": imgDetail.image_dislike }
    return JsonResponse(jsonContent, json_dumps_params={'ensure_ascii': False})

def index(request) :
    return render(request, "index.html")

def generic(request) :
    return render(request, "generic.html")

def elements(request) :
    return render(request, "elements.html")