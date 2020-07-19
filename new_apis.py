from random import choice
import json
import requests
from countries import getCountryCode
from Provincia import API_Provincia

def api_call(url):
	return requests.get(url).json()

def globales(info, lugar):

	equivalents = {
		'infectados': 'TotalConfirmed',
		'recuperados': 'TotalRecovered',
		'fallecidos': 'TotalDeaths'
	}
	url = 'https://api.covid19api.com/world/total'
	response = api_call(url)
	number = '{:,}'.format(response[equivalents[info]])
	mensajes = 	[
					'El numero de '+info+' a nivel global es '+ number + '.'
				]
	text = choice(mensajes) 
	return text

def pais(info, lugar):
	equivalents = {
		'infectados': 'confirmed',
		'recuperados': 'deaths',
		'fallecidos': 'recovered'
	}

	pais = lugar

	try:
		pais = getCountryCode(pais)
	except:
		pais = pais

	url = 'https://api.covid19api.com/total/country/' + pais + '/status/' + equivalents[info]
	response = api_call(url)
	number = '{:,}'.format(response[-1]['Cases'])
	mensajes = [
								'El numero de '+info+' en '+ pais+ ' es de '+ number + '.'
							]
	text = choice(mensajes)
	return text


def provincia(info, prov):	
	api = API_Provincia(prov)
	number = api.get(info)
	mensaje = 'El numero de '+info+' en '+ prov.replace('-', ' ')+ ' es de '+ number + '.'
	return mensaje

endpoints = {
	'globales': globales,
	'pais': pais,
	'provincia': provincia
}

def interpret_watson_response(resp):
	print(resp)
	text = resp['output']['generic'][0]['text']
	
	if 'API' in text:
		intent = resp['output']['intents'][0]['intent']
		try:
			entity = resp['output']['entities'][0]['entity']
			lugar = resp['output']['entities'][0]['value'] 
		except:
			entity = 'globales'
			lugar = None
		response = endpoints[entity](intent, lugar)
		
		return response

	return text