from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def menuapp(request):
  return render(request, 'menuapp.html')
