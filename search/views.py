from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from random import shuffle
import time
import os

from search.models import Pokedex

def srch2(request, foo):
	search_string = str(foo) or '1'
	print type(search_string)

	list_dir = os.listdir(os.path.join(settings.STATIC_PATH,'images'))
	result_arr = []

	for file_name in list_dir:
		if search_string in file_name:
			result_arr.append(file_name)

	context_dict = {}
	context_dict['list_dir'] = list_dir
	context_dict['search_string'] = search_string
	context_dict['result_arr'] = result_arr
	
	return render(request,'search/search.html',context_dict)

def srch(request):
	search_string = request.GET.get("text") or ''
	print type(search_string)
	search_string = str(search_string)

	list_dir = os.listdir(os.path.join(settings.STATIC_PATH,'images'))
	result_arr = []

	for file_name in list_dir:
		if search_string in file_name:
			result_arr.append(file_name)

	context_dict = {}
	context_dict['list_dir'] = list_dir
	context_dict['search_string'] = search_string
	context_dict['result_arr'] = result_arr
	
	return render(request,'search/search.html',context_dict)

def index(request):

	today_date = time.ctime()
	context_dict = {}
	context_dict['date'] = today_date

	list_dir = os.listdir(os.path.join(settings.STATIC_PATH,
		'images'))
	shuffle(list_dir)

	context_dict['list_dir'] = list_dir
	context_dict['pokedex'] = Pokedex.objects.all()
	
	return render(request,'search/index.html',context_dict)

def random(request):
	list_dir = os.listdir(os.path.join(settings.STATIC_PATH,'images'))
	shuffle(list_dir)
	context_dict = {}
	context_dict['list_dir'] = list_dir
	return render(request, 'search/random.html', context_dict)