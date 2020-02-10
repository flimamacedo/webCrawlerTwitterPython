from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from  datetime import datetime
from django.db.models import Sum

from login.models import homeImagens

def index(request):
   # return render(request, 'login/login.html')
    if not request.user.is_authenticated:
        return render(request, 'login/login.html')
    else:
        data = datetime.now()
        imagens = homeImagens.objects.filter(status = 'Ativo').all()
        
        return render(request, 'login/index.html',
            {
                'data': data,
                'imagens': imagens,
            }
        )

def index2(request):
   # return render(request, 'login/login.html')
    data = datetime.now()
    return render(request, 'login/index2.html',
        {
            'data': data,
        }
    )

def login_user(request):
   if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(username=username, password=password)
       if user is not None:
           if user.is_active:
               login(request, user)
               data = datetime.now()	
               imagens = homeImagens.objects.filter(status = 'Ativo').all()
               return render(request, 'login/index.html',
                   {
                        'data': data,
                        'imagens': imagens,
                   }
               )
           else:
               return render(request, 'login/login.html', {'error_message':'Your account has been disabled'})
       else:
           return render(request, 'login/login.html', {'error_message': 'Login invalido'})
   return render(request, 'login/login.html')

def logout_user(request):
   logout(request)
   form = UserForm(request.POST or None)
   context = {
       "form": form,
   }
   return render(request, 'login/login.html', context)

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'login/login.html', {'success_message': 'Conta criada com sucesso! Digite suas credenciais acima.'})
    context = {
        "form": form,
    }
    return render(request, 'login/register.html', context)

def homeCarroussel(request):
    data = datetime.now()
    imagens = homeImagens.objects.filter(status = 'Ativo').all()
    return render(request, 'login/index2.html',
        {
            'data': data,
            'imagens': imagens,
			
        }
    )
