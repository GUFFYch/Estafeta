from cmath import phase
from itertools import count
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import *
from django.shortcuts import render, redirect

from .forms import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404, HttpResponseNotFound
from .forms import *
from django.contrib.auth import authenticate, login
from account.models import Account


def profileTemplate_page(request ,name):
    content = {}

    path = f"profile/template{name}.html"
    if name == '1':
        pass

    elif name == '2':
        pass

    return render(request, path, content)



def profile_page(request):
    content = {}
    try:
        email = request.user
        person = Account.objects.get(email=email)
        content['user'] = person
        return render(request, 'profile.html', content)

    except Account.DoesNotExist:
        print("---------------")
        print("PROBLEMS")
        print("---------------")

def createtest_page(request):
    if request.method == 'POST' and 'submitBtn' in request.POST:
        
        test = Tests()
        test.name = request.POST['name']
        test.subject = request.POST['subject']
        test.level = request.POST['level']
        test.link = request.POST['link']
        test.date_start = request.POST['date_start']
        test.time_start = request.POST['time_start']
        test.date_end = request.POST['date_end']
        test.time_end = request.POST['time_end']
        test.save()
        return HttpResponseRedirect('/createtest/')
    return render(request, 'createtest.html')

def index(request):
    return render(request, 'index.html')

def main_page(request):
    content = {}
    tests = Tests.objects.all()
    content['tests'] = tests
    return render(request, 'main.html', content)

def logout_view(request):
    return HttpResponseRedirect("/")

def reg_page(request):
    form = SignUpForm(request.POST)
    context = {
        'form': form
    }
    # вход

    if request.method == 'POST' and 'profile_saver3' in request.POST:
        # print(form.errors)
        # print(form.is_valid())
        list = request.POST.getlist('sports')

        print(list)


        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            password = form.cleaned_data.get('password1')

            phone = request.POST.get('phone')
            country = request.POST.get('country')
            subjects = request.POST.getlist('sports')
            knowledge = request.POST.get('knowledge')

            user = authenticate(email=email, password=password,
             first_name=first_name)

            user.phone = phone
            user.country = country
            user.knowledge = knowledge
            user.subjects = subjects
            print(request.POST)
            user.save()
            return redirect('/login/')

  

    return render(request, 'signin.html', context)

def login_page(request):
    print(request.POST)

    if request.method == 'POST' and 'btnform2' in request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('Try again! username or password is incorrect')
    return render(request, 'login.html')