from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from movieapp.models import Movie


def index(request):
    obj = Movie.objects.all()
    return render(request,'index.html',{'movielist':obj})

def detail(request,id):
    obj = Movie.objects.get(id=id)
    return render(request,'detail.html',{'result':obj})

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        image = request.FILES['image']
        movie = Movie(name=name,desc=desc,year=year,image=image)
        movie.save()

    return render(request,'add.html')