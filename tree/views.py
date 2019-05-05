from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .utils import get_json_tree


@login_required(login_url='/admin/login/?next=/')
def index(request):
	context = {"json_tree": get_json_tree()}
	return render(request, 'tree/index.html', context)	

@login_required(login_url='/admin/login/?next=/')
def fetch_json_tree(request):
	return HttpResponse(get_json_tree())
    