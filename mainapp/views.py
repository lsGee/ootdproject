from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from mainapp.models import Sido, City, Image
from django.core.paginator import Paginator
from django.templatetags.static import static
from datetime import date
from django.db.models import Sum

# Create your views here.
def main(request) :
    today = date.today()
    todayImg = Image.objects.filter(image_date__month=today.month, image_date__day=today.day)
    today_like = todayImg.aggregate(Sum("image_like"))["image_like__sum"]
    today_dislike = todayImg.aggregate(Sum("image_dislike"))["image_dislike__sum"]
    try:
        image_plike = int(today_like/(today_dislike + today_like)*100)
    except:
        image_plike = 0

    context = {
        'sido_geo': static("sido.geojson"),
        'sigungu_geo': static("sigungu.geojson"),
        'sido_list': Sido.objects.all(),
        'city_list': City.objects.all(),
        'image_list': todayImg.order_by("city_id", "image_cnt"),
        'image_list_like': todayImg.order_by("city_id", "image_like")[:5],
        'image_count': todayImg.count(),
        'image_plike': image_plike,
    }

    return render(request, "main.html", context)
