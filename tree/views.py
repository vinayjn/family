from django.shortcuts import render

from django.http import HttpResponse
from .utils import get_json_tree

def index(request):
	return HttpResponse(get_json_tree())
