from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html' );

def articles(request, year):
    return HttpResponse('O ano de envio foi: '+str(year))

def lerDoBanco(nome,opc ):
    lista_nome =[
        {'nome': 'Vitor','idade':19},
        {'nome': 'Loids', 'idade': 20},
        {'nome': 'Ana Laura', 'idade': 16}
    ]
    if opc==1:
        for pessoa in lista_nome:
            if pessoa['nome'] == nome:
                return {'nome':pessoa['nome'] + ' tem ' + str(pessoa['idade']) + ' anos', }
            else:
                return {'Pessoa nao encontrada'}
    else:
        for pessoa in lista_nome:
            if pessoa['nome'] == nome:
                return pessoa
            else:
                {'nome':'Jenifer','idade':'bang'}
def fname(request, nome):
    return HttpResponse(lerDoBanco(nome,1))

def fname2(request, nome):
    idade = lerDoBanco(nome,2)
    print(idade)
    return render(request, 'pessoa.html',
                  {'v_idade':idade['idade'],'v_nome':idade['nome']}
                  )