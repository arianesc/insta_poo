from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import authenticate, login, get_user_model
import re
from .forms import LoginForm
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Foto
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

User = get_user_model()

@csrf_protect
def login(request):
    login_form = LoginForm()
    context = {}
    

    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = re.findall(r'\d', request.POST['username'])
            user = authenticate(request,
                                username=username,
                                password=request.POST['password'])

    context['login_form'] = login_form

    return render(request, 'perfil.html', context)


@login_required
def logout(request):
    auth_logout(request)

    return redirect(reverse('login'))

class FotoForm(ModelForm):
    class Meta:
        model = Foto
        fields = ['legenda', 'imagem']

def feed(request, template_name='core/foto_list.html'):
    foto = Foto.objects.all()
    data = {}
    data['object_list'] = foto
    return render(request, template_name, data)

def View(request, pk, template_name='core/foto_detail.html'):
    foto = get_object_or_404(Foto, pk=pk)    
    return render(request, template_name, {'object':foto})

def Create(request, template_name='core/foto_form.html'):
    form = FotoForm(request.POST or None)
    if form.is_valid():

        legenda = request.POST.get('legenda')
        imagem = request.POST.get('imagem')
        Foto.objects.create(legenda=legenda,imagem=imagem)
  
        return redirect('foto_list')
    return render(request, template_name, {'form':form})

def Update(request, pk, template_name='core/foto_form.html'):
    foto = get_object_or_404(Foto, pk=pk)
    form = FotoForm(request.POST or None, instance=foto)
    if form.is_valid():
        form.save()
        return redirect('foto_list')
    return render(request, template_name, {'form':form})

def Delete(request, pk, template_name='core/foto_confirm_delete.html'):
    foto = get_object_or_404(Foto, pk=pk)    
    if request.method=='POST':
        foto.delete()
        return redirect('foto_list')
    return render(request, template_name, {'object':foto})

    
