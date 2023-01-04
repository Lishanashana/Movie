from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import Movieform

# Create your views here.
def index(request):
    movie=Movie.objects.all()    #models fetching as dictionary to display on the front end
    context={
        'movielist':movie
    }
    return render(request,'index.html',context)

def detail(request,movieid):  #for showing details when schoose movie id
    movie=Movie.objects.get(id=movieid)
    return render(request,'detail.html',{'movie':movie})


def add(request):
    add=Movie.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        description = request.POST.get('description')
        year = request.POST.get('year')
        image = request.FILES['image']
        movie=Movie(name=name ,description=description,year=year,image=image)
        movie.save()
    return render(request,'add.html',{'add':add})

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=Movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=="POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')