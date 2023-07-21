from django.shortcuts import render
from django.contrib import messages
from .models import *
from django.core.files.storage import FileSystemStorage
# Create your views here.


def programs(request):
    context = {"all_programs": Program.objects.all()}
    return render(request, "programs.html", context)


def new_program(request):
    return render(request, "new_program.html")


def create_program(request):

    if request.method == "POST" and request.FILES['image']:
        photo = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(photo.name, photo)
        file_url = fss.url(file)
        Program.objects.create(
            name=request.POST['name'],
            availability=request.POST['availability'],
            description=request.POST['description'],
            image=file_url)
        return redirect('/programs')


def edit_program(request, id):
    context = {'program': Program.objects.get(id=id).__dict__}
    return render(request, 'edit_program.html', context)


def update_program(request, id):
    if request.method == "POST":
        program = Program.objects.get(id=id)
        program.name = request.POST['name']
        program.availability = request.POST['availability']
        program.description = request.POST['description']
        program.save()
        return redirect(f'/programs/{id}')
    return redirect(f'programs/{id}')
