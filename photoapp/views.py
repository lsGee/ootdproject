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
            context = { "alist": aListpage, "aDetail": aDetail, "sort": sort, "data": data }
        except Image.DoesNotExist:
            context = {"msg": "게시물이 존재하지 않습니다."}

        return render(request, "photo.html", context)

    elif data == "today" or data == "allday" or data == "" :
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
            context = { "imageList": imageListpage, "imgDetail": imgDetail, "sort": sort, "data": data }


        except Image.DoesNotExist :
            context = { "msg" : "게시물이 존재하지 않습니다." }

        return render(request, "photo.html", context)

    elif data == "top5" :
        try:
            blistA = Image.objects.filter(image_date__month=today.month,
                                             image_date__day=today.day).order_by('image_like').reverse()
            blist = blistA[:5]
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

    elif data == "cnt" :
        try :
            if sort !="" :
                cList = Image.objects.filter(city_id_id= city,
                                                 image_date__month=today.month,
                                                 image_date__day=today.day).order_by(sort).reverse()
            else:
                cList = Image.objects.filter(city_id_id=city,
                                                 image_date__month=today.month,
                                                 image_date__day=today.day).order_by('image_date').reverse()

            cDetail = cList[list]
            cDetail.image_cnt += 1;
            cDetail.save()
            page = request.GET.get('page',list+1)
            print(cDetail)
            paginator = Paginator(cList,1)
            cListpage = paginator.get_page(page)
            context = { "cList": cListpage, "cDetail": cDetail, "sort": sort, "data": data }


        except Image.DoesNotExist :
            context = { "msg" : "게시물이 존재하지 않습니다." }

        return render(request, "photo.html", context)

    else :
        return redirect("main")

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
