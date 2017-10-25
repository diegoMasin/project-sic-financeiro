from django.shortcuts import render

titulo_pagina = 'Home'
namespace = 'pagina_inicial'
menu = 'home'
context = {
    'titulo_pagina': titulo_pagina,
    'namespace': namespace,
    'menu': menu,
}


def pagina_inicial(request):
    return render(request, '{0}/index.html'.format(namespace), context)
