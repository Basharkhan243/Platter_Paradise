from django.shortcuts import render

def Mainhome(request):
  return render(request, 'index.html')

def loginn(request):
  return render(request, 'login.html')