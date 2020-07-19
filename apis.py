#ESTE SCRIPT YA NO SE USA
#DEPRACATED

from random import choice
import json
import requests
from countries import getCountryCode
from api_provincias import provincia

def api_call(url):
	return requests.get(url).json()

def casos_globales(param):
	url = 'https://api.covid19api.com/world/total'
	response = api_call(url)
	number = '{:,}'.format(response['TotalConfirmed'])
	mensajes = [
								'El numero de infectados a nivel global es '+ number + '.', 
								'Hay ' + number + ' personas infectadas en el mundo.'
							]
	text = choice(mensajes) 
	return text

def casos_pais(pais):
	try:
		pais = getCountryCode(pais)
	except:
		pais = pais
	url = 'https://api.covid19api.com/total/country/'+pais+'/status/confirmed'
	response = api_call(url)
	number = '{:,}'.format(response[-1]['Cases'])
	mensajes = [
								'El numero de infectados en '+ pais+ ' es de '+ number + '.', 
								'Hay ' + number + ' personas infectadas en ' +pais +'.'
							]
	text = choice(mensajes)
	return text
	
def casos_provincia(prov, info='Casos'):
	number = str(info_provincias(prov, info)[1])
	mensajes = [
								'El numero de infectados en '+ pais+ ' es de '+ number + '.', 
								'Hay ' + number +  ' personas infectadas en ' +pais +'.'
							]
	text = choice(mensajes) 
	return text