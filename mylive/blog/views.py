from django.shortcuts import render
from djanjo.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'blog/index.html')
