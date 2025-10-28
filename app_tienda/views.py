from django.shortcuts import render, get_object_or_404, redirect
from .models import Tienda
from .forms import TiendaForm

def ver_tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request, 'ver_tiendas.html', {'tiendas': tiendas})

def info_tienda(request, tienda_id):
    tienda = get_object_or_404(Tienda, id=tienda_id)
    return render(request, 'info_tienda.html', {'tienda': tienda})

def agregar_tienda(request):
    if request.method == 'POST':
        form = TiendaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_tienda:ver_tiendas')
    else:
        form = TiendaForm()
    return render(request, 'formulario_tienda.html', {'form': form, 'titulo': 'Crear Tienda'})

def editar_tienda(request, tienda_id):
    tienda = get_object_or_404(Tienda, id=tienda_id)
    if request.method == 'POST':
        form = TiendaForm(request.POST, request.FILES, instance=tienda)
        if form.is_valid():
            form.save()
            return redirect('app_tienda:info_tienda', tienda_id=tienda.id)
    else:
        form = TiendaForm(instance=tienda)
    return render(request, 'formulario_tienda.html', {'form': form, 'titulo': 'Editar Tienda'})

def borrar_tienda(request, tienda_id):
    tienda = get_object_or_404(Tienda, id=tienda_id)
    if request.method == 'POST':
        tienda.delete()
        return redirect('app_tienda:ver_tiendas')
    return render(request, 'confirmar_borrar.html', {'tienda': tienda})