from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseServerError
from .models import Agent, Client, Contract, Object, Office, Rate
from .forms import EmailForm

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def rates(request):
    rates_db = Rate.objects.order_by('tariff_name')
    return render(request, 'main/rates.html', {'rates': rates_db})

def agents(request):
    agents_db = Agent.objects.order_by('full_name')
    return render(request, 'main/agents.html', {'agents': agents_db})

def contacts(request):
    offices_db = Office.objects.order_by('office_name')
    return render(request, 'main/contacts.html', {'offices': offices_db})

def email_from_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            send_mail(
                "Новое обращение",
                f'Пользователь оставил следующий e-mail: {user_email}',
                "tigranmogikan@outlook.com",
                ["tigranmogikan@mail.ru"],
                fail_silently=False,
            )
            return redirect('home')
    else:
        form = EmailForm()

    return render(request, 'main/email_form.html', {'form': form})

def badRequest(request, exception):
    return HttpResponseBadRequest('<h1>Неудачный запрос</h1>') #400

def forbidden(request, exception):
    return HttpResponseForbidden('<h1>Доступ запрещён</h1>') #403

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Статья не найдена</h1>') #404

def internalServerError(request):
    return HttpResponseServerError('<h1>Ошибка сервера</h1>') #500
