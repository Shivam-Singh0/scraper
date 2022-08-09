
from http.client import HTTPResponse
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect

# Create your views here.

def scarp(request):
    if request.method == 'POST':
        page = request.POST.get("site", '')
        page = requests.get(page)
        soup = BeautifulSoup(page.text, 'html.parser')

        for link in soup.find_all('a'):
            link_add = link.get('href')
            link_text = link.string
            Link.objects.create(add=link_add, name=link_text)
        return HttpResponseRedirect('/')

    else:
        data = Link.objects.all()

    return render(request, 'result.html', {'data':data})


def clear(request):
    Link.objects.all().delete()
    return render(request, 'result.html')