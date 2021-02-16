from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Index Page")
def home(request):
    diction = {'demo':'I am a demo-text'}
    return render(request, 'first_app/index.html',context=diction)
