from django.shortcuts import render

from django.http import HttpResponse
from .utils import get_json_tree

def index(request):
	context = {"json_tree": get_json_tree()}
	return render(request, 'tree/index.html', context)	

def fetch_json_tree(request):
	return HttpResponse(get_json_tree())
    