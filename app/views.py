"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contato',
            'message':'Entre em contato conosco',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Gerenciador de vestibulares',
            'year':datetime.now().year,
        })
    )

def cadastro_cursos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cadastro_cursos.html',
        context_instance = RequestContext(request,
        {
            'title':'Cadastro de cursos',
            'cursos': ['ADS' , 'SI', 'CC'],
            'year':datetime.now().year,
        })

    )

def criacao_vestibulares(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/criacao_vestibulares.html',
        context_instance = RequestContext(request,
        {
            'title':'Criacao de Vestibulares',
            'cursos2': ['ADS' , 'Sistemas de Informacao', 'Administracao'],
            'year':datetime.now().year,
            'mounth':datetime.now().mounth,
        })

    )

