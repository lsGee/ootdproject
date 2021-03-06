from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from mainapp.models import Sido, City, Image
from django.core.paginator import Paginator
from django.templatetags.static import static


# Create your views here.


# Create your views here.
def upload(request):
    context = None
    if request.method == 'POST':
        image = Image(image_name=request.POST['image_name'],
                      image_like=0,
                      image_dislike=0,
                      image_cnt=0,
                      city_id_id=request.POST.get('city_id', ''),
                      sido_id_id=City.objects.filter(city_id=request.POST.get('city_id', '')).values('sido_id'),
                      image_file=request.FILES['image_file'])
        image.save()

        context = {"image": image}
        context = {'sido_list': Sido.objects.all(),
                   'city_list': City.objects.all()}
    else:
        context = {'sido_list': Sido.objects.all(),
                   'city_list': City.objects.all()}

    return render(request, "upload.html", context)


def uploadsel(request):
    context = None
    if request.method == 'POST':
        image = Image(image_name=request.POST['image_name'],
                      image_like=0,
                      image_dislike=0,
                      image_cnt=0,
                      city_id_id=request.POST.get('city_id', ''),
                      sido_id_id=request.POST.get('sido_id', ''),
                      image_file=request.FILES['image_file'])
        image.save()
        context = {"image": image}
        context = {'sido_list': Sido.objects.all(),
                   'city_list': City.objects.all()}

    else:
        context = {'sido_list': Sido.objects.all(),
                   'city_list': City.objects.all()}

    return render(request, "upload.html", context)