from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
import time
import os
from django.conf import settings

from random import shuffle

# Create your views here.

def index(request):
	today_date = time.ctime()
	context_dict = {}
	context_dict['date'] = today_date

	list_dir = os.listdir(os.path.join(settings.STATIC_PATH,'images'))
	shuffle(list_dir)

	context_dict['list_dir'] = list_dir
	
	print list_dir
	return render(request,'search/index.html',context_dict)

def random(request):
	list_dir = os.listdir(os.path.join(settings.STATIC_PATH,'images'))
	shuffle(list_dir)
	context_dict = {}
	context_dict['list_dir'] = list_dir
	return render(request, 'search/random.html', context_dict)