from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index2(request):
    return HttpResponse("<h1> hello world</h1>")
def sample2(request):
    return render(request,'app2/sample2.html')