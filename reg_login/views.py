from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.


def index(request):
    return render(request, "index.html")


def reg_form(request):
    return render(request, 'reg.html')


def create_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/reg')
    elif request.method == "POST":
        pw = request.POST['pw']
        pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            fname=request.POST['fname'],
            lname=request.POST['lname'],
            email=request.POST['email'],
            dob=request.POST['dob'],
            pw=pw_hash)
        request.session['user_id'] = new_user.id
        return redirect('/dash')


def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0].__dict__
        if bcrypt.checkpw(request.POST['pw'].encode(), logged_user['pw'].encode()):
            request.session['user_id'] = logged_user['id']
            print(request.session['user_id'])
            print(logged_user)
            return redirect('/dash')
    return redirect('/')


def dash(request):
    if request.session['user_id']:
        user = User.objects.get(pk=request.session['user_id']).__dict__
        print(request.session['user_id'])
        return render(request, 'dash.html', user)
    return redirect('/')


def edit_user(request):
    context = {'user': User.objects.get(
        id=request.session['user_id']).__dict__}
    return render(request, 'edit_user.html', context)

def update_user(request):
    if request.method == "POST":
        user = User.objects.get(id=request.session['user_id'])
        user.fname = request.POST['fname']
        user.lname = request.POST['lname']
        user.email = request.POST['email']
        user.dob = request.POST['dob']



def logout(request):
    del request.session['user_id']
    return redirect('/')
