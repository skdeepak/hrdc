from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello, World. You are at the polls index.")

def homepage(request):
	#return render('/index.html')
	return render_to_response('index.html')


