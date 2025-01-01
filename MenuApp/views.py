from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ImageData
from .models import SearchQuery
from .forms import SearchForm
# Create your views here.
def menuapp(request):
  
  res = ImageData.objects.all()
  return render(request, 'menuapp.html', {'res': res})



def menuapp(request):
  if request.method == 'POST':
    form = SearchForm(request.POST)
    print(form.is_valid())  # Add this print statement
    if form.is_valid():
      query = form.cleaned_data['search']
      SearchQuery.objects.create(query=query)
  res = ImageData.objects.all()
  return render(request, 'menuapp.html', {'res': res})