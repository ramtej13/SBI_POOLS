from django.shortcuts import render
from .forms import Contact_Forms
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        form = Contact_Forms(request.POST)
        if form.is_valid():
            print("is valid")
            obj = form.save(commit=False)
            obj.save()
            return HttpResponseRedirect('/')
    return render(request, 'index.html')

def form(request):
    if request.method == 'POST':
        form = Contact_Forms(request.POST)
        if form.is_valid():
            print("is valid")
            obj = form.save(commit=False)
            obj.save()
            return HttpResponseRedirect('/form')
    else:
        form = Contact_Forms()
    return render(request, 'form.html', {'form': form})

