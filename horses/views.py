from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.core.files.storage import FileSystemStorage
# Create your views here.


def horses_main(request):
    horses = {"all_horses": Horse.objects.all()}
    return render(request, "horses_main.html", horses)


def horse_bio(request, id):
    horses = {"all_horses": Horse.objects.all(),
              "one_horse": Horse.objects.get(id=id).__dict__}
    return render(request, "horse_bio.html", horses)


def new_horse(request):
    return render(request, "new_horse.html")


def create_horse(request):

    if request.method == "POST" and request.FILES['image']:
        photo = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(photo.name, photo)
        file_url = fss.url(file)
        Horse.objects.create(
            name=request.POST['name'],
            age=int(request.POST['age']),
            breed=request.POST['breed'],
            description=request.POST['description'],
            image=file_url)
        return redirect('/horses')


def edit_horse(request, id):
    context = {'horse': Horse.objects.get(id=id).__dict__}
    return render(request, 'edit_horse.html', context)


def update_horse(request, id):
    if request.method == "POST":
        horse = Horse.objects.get(id=id)
        horse.name = request.POST['name']
        horse.age = request.POST['age']
        horse.breed = request.POST['breed']
        horse.save()
        return redirect(f'/horses/{id}')
    return redirect(f'horses/{id}')
