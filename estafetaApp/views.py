from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404, HttpResponseNotFound

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
    if request.method == 'POST' and 'btnform2' in request.POST:
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
        send_mail(
            'Test',
            'Всё робит)',
            'korotikhin84@mail.ru',
            ['gaamer557@gmail.com'],
            fail_silently=False,
        )
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            username = email
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password, first_name=first_name)
            # login(request, user)
            return redirect('/login/')
        else:
            print(form.errors)

    return render(request, 'signin.html', context)