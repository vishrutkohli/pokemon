
import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pokemonGo.settings')
os
import django 
django.setup()

from search.models import Pokedex
from search.views import search_pokemon

def populate():
	    for pokemon in search_pokemon('*',result_type='dict'):
	    	add(pokemon_name = pokemon['name'],
	    		pokemon_image=pokemon['image_url'])


	

def showDB():
	for pokemon in Pokedex.objects.all():
		print pokemon

def add(pokemon_name,pokemon_image,pokemon_type='N/A'):
    p=Pokedex.objects.get_or_create(pokemon_name=pokemon_name,pokemon_image=pokemon_image,pokemon_type =pokemon_type)[0]
    p.save()
    showDB()		 




if __name__ == '__main__':
	populate()
	    


	

