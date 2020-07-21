from random import choice
import requests
from countries import natural
from Provincia import API_Provincia
from contacto import mensaje_contacto

def api_call(url):
	return requests.get(url).json()

def globales(info, lugar, fecha):
	equivalents = {
		'infectados': 'TotalConfirmed',
		'recuperados': 'TotalRecovered',
		'fallecidos': 'TotalDeaths'
	}
	url = 'https://api.covid19api.com/world/total'
	response = api_call(url)
	number = '{:.}'.format(response[equivalents[info]])
	mensajes = 	[
					'El numero de '+info+' a nivel global es '+ number + '.'
				]
	text = choice(mensajes) 
	return text

def pais(info, pais, fecha=None):
	equivalents = {
		'infectados': 'confirmed',
		'recuperados': 'recovered',
		'fallecidos': 'deaths'
	}
	url = 'https://api.covid19api.com/total/country/' + pais + '/status/' + equivalents[info]
	response = api_call(url)
	if fecha is None:
		number = response[-1]['Cases']
		if number > 999:
			number = '{:,}'.format(number).replace(',', '.')
		mensajes = 'El numero de '+info+' en '+ natural[pais]+ ' es de '+ str(number) + '.'
		text = mensajes
		return text
	for count, register in enumerate(response):
		entered_date = "2020-"+fecha+"T00:00:00Z" 
		if register['Date'] == entered_date:			
			number = int(register['Cases']) - int(response[count-1]['Cases'])
			if number > 999:
				number = '{:,}'.format(number).replace(',', '.')
			return 'El numero de '+info+' en '+ natural[pais]+ ' el '+fecha+' es de '+ str(number) + '.'
	return 'No contamos con ese registro'


def provincia(info, prov, fecha):	
	api = API_Provincia(prov)
	number = str(api.get(info))
	prov = api.provincia
	prov = prov.replace('-', ' ')
	if prov in api.correciones.keys():
		prov = api.correciones[prov]
	mensaje = 'El numero de '+info+' en '+ prov + ' es de '+ number.replace(',', '.') + '.'
	return mensaje

endpoints = {
	'globales': globales,
	'pais': pais,
	'provincia': provincia
}

def interpret_watson_response(resp):
	print(resp)
	text = resp['output']['generic'][0]['text']
	entity = 'globales'
	lugar = None
	fecha = None
	
	if 'API' in text:
		confidence = 0
		try:
			intent = resp['output']['intents'][0]['intent']
			confidence = resp['output']['intents'][0]['confidence']

		except:

			None
		if confidence < 0.5:

			intent = resp["context"]["skills"]["main skill"]["user_defined"]['intencion']

		print(intent)
		try:
			entities = list(resp["context"]["skills"]["main skill"]["user_defined"].keys())
			for entity_ in entities:
				lugar = resp["context"]["skills"]["main skill"]["user_defined"][entity_]
				if lugar is not None and entity_ != 'intencion':
					entity = entity_
					break
		except:
			None
		try:
			entity = resp['output']['entities'][0]['entity']
			lugar = resp['output']['entities'][0]['value'] 
		except:
			None
		print(intent, entity, lugar)
		response = endpoints[entity](intent, lugar, fecha)
		
		return response

	if 'Contacto' in text:
		provincia = resp['output']['entities'][0]['value'] 
		print(provincia)
		return mensaje_contacto(provincia)

	if 'Fecha' in text:
		pais = resp["context"]["skills"]["main skill"]["user_defined"]['pais']
		fecha = resp["context"]["skills"]["main skill"]["user_defined"]['fecha']
		intencion = resp["context"]["skills"]["main skill"]["user_defined"]['intencion']
		print(intencion, pais, fecha)
		return endpoints['pais'](intencion, pais, fecha)

	return text