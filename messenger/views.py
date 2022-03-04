from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, response, Http404, HttpResponseRedirect


# Create your views here.


def index(request):
    return render(request, 'messenger/index.html')
