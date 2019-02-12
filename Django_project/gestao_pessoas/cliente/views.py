from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cliente.models import Person
from .forms import ClientsForm

# Create your views here.

@login_required
def person_list(request):
    persons = Person.objects.all()
    return render(request, 'clients.html',{'clientes':persons})


@login_required
def person_new(request):
    form= ClientsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
       form.save()
       return redirect('nick_list')
    return render(request, 'clients_form.html',{'form':form})

@login_required
def person_up(request,id):
    client = get_object_or_404(Person, pk=id)
    form = ClientsForm(request.POST or None, request.FILES or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('nick_list')
    return render(request, 'clients_form.html',{'form':form})

@login_required
def person_del(request,id):
    client = get_object_or_404(Person, pk=id)
    form = ClientsForm(request.POST or None, request.FILES or None, instance=client)

    if request.method == 'POST':
        client.delete()
        return redirect('nick_list')

    return render(request, 'clients_del.html',{'form':form, 'client': client})

