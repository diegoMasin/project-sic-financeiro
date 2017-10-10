from django.shortcuts import render

titulo_pagina = 'Home'
namespace = 'index'
menu = 'home'

context = {
    'titulo_pagina': titulo_pagina,
    'namespace': namespace,
    'menu': menu,
}


def home(request):
    return render(request, 'index.html', context)
