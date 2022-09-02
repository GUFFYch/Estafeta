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
    content = {}
    
    return render(request, 'createtest.html')
def index(request):
    return render(request, 'index.html')

def logout_view(request):
    return HttpResponseRedirect("/")

def login_page(request):
    form = SignUpForm(request.POST)
    context = {
        'form': form
    }
    # вход

    if request.method == 'POST' and 'profile_saver3' in request.POST:
        print(form.errors)
        print(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            first_name = request.POST.get('name')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password, first_name=first_name)
            return redirect('/login/')

    elif request.method == 'POST' and 'btnform2' in request.POST:
        print(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('Try again! username or password is incorrect')
    # регистрация
    elif request.method == 'POST' and 'btnform1' in request.POST:
        print("------------")

        print(form)
        print("------------")

        form.save()
        email = form.cleaned_data.get('email')
        first_name = form.cleaned_data.get('first_name')
        password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=password, first_name=first_name)
        # login(request, user)
        return redirect('/login/')


    return render(request, 'signin.html', context)