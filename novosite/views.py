from django.shortcuts import render, redirect
from novosite.forms import CarroForm
from novosite.models import Carro
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    data = {}
    all_carros = Carro.objects.filter(excluido=False).order_by('id')
    paginator = Paginator(all_carros, 2)
    page = request.GET.get('page')
    data['carros'] = paginator.get_page(page)
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = CarroForm()
    return render(request, 'form.html', data)

def salvar(request):
    form = CarroForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('index')

def visualizar(request, id):
    data = {}
    data['carro'] = Carro.objects.get(id=id)
    return render(request, 'visualizar.html', data)

def editar(request, id):
    data = {}
    data['carro'] = Carro.objects.get(id=id)
    data['form'] = CarroForm(instance=data['carro'])
    return render(request, 'form.html', data)

def update(request, id):
    data = {}
    data['carro'] = Carro.objects.get(id=id)
    form = CarroForm(request.POST or None, instance=data['carro'])
    if form.is_valid():
        form.save()
    return redirect('visualizar', id=id)

def deletar(request, id):
    carro = {}
    carro = Carro.objects.get(id=id)
    carro.excluido = True
    carro.save()
    return redirect('index')