from cmath import phase
from itertools import count
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404, HttpResponseNotFound
from django.contrib.auth import authenticate, login, logout
from account.models import Account
from django.core.files.storage import FileSystemStorage
import openpyxl
from .models import Tests, Team
from django.db.models import Q

def table_page(request):
    content = {}
    if request.FILES:
        excel_file = request.FILES["excel_file"]

        wb = openpyxl.load_workbook(excel_file)

        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()

        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        print(excel_data[1::])

        content["excel_data_start"] = excel_data[0]

        content["excel_data"] = excel_data[1::]

    return render(request, 'tables.html', content)

def profile_page(request):
    content = {}
    try:
        email = request.user
        person = Account.objects.get(email=email)
        content['user'] = person
        if request.method == 'POST' and 'createTeam' in request.POST:
            team = Team()
            team.name = request.POST['name']
            team.language = request.POST['language']
            team.password = request.POST['password']
            team.save()
            return HttpResponseRedirect('/profile/')

        return render(request, 'profile.html', content)

    except Account.DoesNotExist:
        print("---------------")
        print("PROBLEMS")
        print("---------------")

def profileTemplate_page(request, name):
    content = {}
    path = f"profile/template{name}.html"
    return render(request, path, content)


def searchTeam_page(request, name):
    content = {}
    content['teams'] = Team.objects.filter(name__icontains=name)
    return render(request, 'teamslist.html', content)

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
    content = {}
    user = request.user
    print(user)
    content['user'] = user
    return render(request, 'index.html', content)

def main_page(request):
    content = {}
    tests = Tests.objects.all()
    content['tests'] = tests
    return render(request, 'main.html', content)

def logout_view(request):
    logout(request)
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
    content = {}
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