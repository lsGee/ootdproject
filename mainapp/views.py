from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from mainapp.models import Sido, City, Image
from django.core.paginator import Paginator
from django.templatetags.static import static

# Create your views here.
def main(request) :
    # cityId_tlist = list(City.objects.values_list('city_id').distinct())
    # cityId_list = []
    # for i in cityId_tlist:
    #     cityId_list.append(i[0])
    #
    # for i in cityId_list:
    #     Image.objects.filter(city_id=i).order_by(image_cnt)[0]

    context = {
        'sido_geo': static("sido.geojson"),
        'sigungu_geo': static("sigungu.geojson"),
        'sido_list': Sido.objects.all(),
        'city_list': City.objects.all(),
        'image_list': Image.objects.all().order_by("city_id", "image_cnt"),
        'image_count': Image.objects.count()
    }

    return render(request, "main.html", context)
