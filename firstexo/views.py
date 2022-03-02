from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import Question
from django.utils import timezone

from .forms import questionform


def index(request):
    questions = Question.objects.all()
    return render(request, 'firstexo/index.html', {'questions': questions})


def create(request):
    if request.method == "POST":
        text = request.POST['text']
        question = Question.objects.create(text=text)
        question.save()
        return redirect('/firstexo/')
    return render(request, 'firstexo/create.html')


def edit(request, id):
    question = Question.objects.get(id=id)
    return render(request, 'firstexo/edit.html', {'object': question})


def update(request, id):
    question = Question.objects.get(id=id)
    form = questionform(request.POST, instance=question)
    if form.is_valid:
        form.save()
        return redirect('/firstexo/')


def delete(request, id):
    Question.objects.filter(id=id).delete()
    return redirect('/firstexo/')
