from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saludo(resquest):
    document = """<html>
    <head>
    Hola
    </head>
    <body>
    </body>
    </html>"""
    return HttpResponse(document)
