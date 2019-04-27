from django.shortcuts import render

from django.http import HttpResponse
from .utils import get_json_tree

def index(request):
	members = Member.objects.all()
	queue = [members[0]]
    return HttpResponse(get_json_tree())