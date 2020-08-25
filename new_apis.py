from random import choice
import requests
#from countries import natural
#from contacto import mensaje_contacto
from resources import natural, mensaje_contacto, traduccion
from Provincia import API_Provincia
import difflib
from bs4 import BeautifulSoup
import pickle
from datetime import datetime

class Globales:

	results = {}
	registers_label = 'Empty'

	def __init__(self):
		self.results = {}

	def count(self):
		self.registers_label = len(self.results.keys())+' registros.'

	def __str__(self):
		return self.registers_label

	def __repr__(self):
		return self.registers_label

	def load(self):
		url = "https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory"
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		noise = soup.find('caption')
		noise.decompose()


		noise = soup.find_all('td', attrs={'style':'padding:0px 2px;'})
		for td in noise:
			td.decompose()

		noise = soup.find_all('img')
		for img in noise:
			img.decompose()
		
		noise = soup.find_all("tr", class_="sortbottom")
		for tr in noise:
			tr.decompose()

		table = soup.find("table", class_="wikitable")

		rows = table.find_all('tr')

		cases, deaths, recov = [title.text.replace('\n', '').replace(',', '.') for title in rows[1].find_all('th')[1:6]][1:4]
		active = int(cases.replace('.', '')) - (int(deaths.replace('.', ''))+int(recov.replace('.', '')))

		self.results['world'] = 	{
								'infectados':cases,
								'fallecidos':deaths,
								'recuperados':recov,
								'activos': active
							}

		rows = rows[2:]

		for row in rows:
			country = row.find_all('th')[1].text.replace('\n', '')
			if '[' in country:
				country = country.split('[')[0]
			res = [title.text.replace('\n', '') for title in row.find_all('td')[0:3]]

			done = False
			for i in range(len(res)):
				if res[i] == 'No data':
					self.results[country] = 	{
											'infectados':cases,
											'fallecidos':deaths,
											'recuperados':recov,
											'activos': '-'
										}
					done = True
				if ',' in res[i]:
					res[i] = res[i].replace(',', '.')
			if not done:
				done = False
				cases, deaths, recov = res
				active = int(cases.replace('.', '')) - (int(deaths.replace('.', ''))+int(recov.replace('.', '')))
				if active > 999:
					active = '{:,}'.format(active).replace(',', '.')
				self.results[country] = 	{
										'infectados':cases,
										'fallecidos':deaths,
										'recuperados':recov,
										'activos': active
									}
	def getCountry(self, country):
		self.load()
		return self.results[country]

	def getCountryInfo(self, country, info):
		self.load()
		return self.results[country][info]

	def getCountryKeys(self):
		self.load()
		return list(self.results.keys())

	def getInfoKeys(self):
		return ['infectados', 'fallecidos', 'recuperados', 'activos']

#Obtains JSON response from api url.
def api_call(url):
	return requests.get(url).json()

#Obtains global case count of confirmed, deaths and recovered from COVID-19 with the use of api.covid19api.com
def globales(info, lugar, fecha=None):
	if fecha:
		return "Estoy trabajando en ello"
	else:
		data = Globales()
		data.load()
		number = data.results['world'][info]
		mensajes = 	[
					'El numero de '+info+' a nivel global es '+ number + '.'
				]
		text = choice(mensajes) 
		return text
	
	"""
	covid19api
	equivalents = {
		'infectados': 'TotalConfirmed',
		'recuperados': 'TotalRecovered',
		'fallecidos': 'TotalDeaths'
	}
	url = 'https://api.covid19api.com/world/total'
	response = api_call(url)
	number = response[equivalents[info]]
	if number > 999:
		number = '{:,}'.format(number).replace(',', '.')
	mensajes = 	[
					'El numero de '+info+' a nivel global es '+ number + '.'
				]
	text = choice(mensajes) 
	return text
	"""

#Obtains case count by country of confirmed, deaths and recovered from COVID-19 with the use of api.covid19api.com
def pais(info, pais, fecha=None):
	if fecha:
		return "Estoy trabajando en ello"
	else:
		date = datetime.today().strftime('%Y-%m-%d')
		data = Globales()
		if pickle.load(open("globales.p", "rb"))['date'] == date:
			data.results = pickle.load(open("globales.p", "rb"))['data']
		else:
			data.load()
		pais = difflib.get_close_matches(pais, data.getCountryKeys(),1)[0]
		number = data.getCountryInfo(pais, info)
		pickle.dump({'data': data.results, 'date': date}, open("globales.p", "wb"))
		#pais = traduccion[pais]
		return 'El numero de ' + info + ' en '+ pais + ' es de '+ number + '.'
	"""
	covid19api
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
	"""

#Obtains case count by Provincia Argentina of confirmed, deaths and recovered from COVID-19 with the use of api.covid19api.com
def provincia(info, prov, fecha):	
	api = API_Provincia(prov)
	number = str(api.get(info))
	prov = api.provincia
	prov = prov.replace('-', ' ')
	if prov in api.correciones.keys():
		prov = api.correciones[prov]
	mensaje = 'El numero de '+info+' en '+ prov + ' es de '+ number.replace(',', '.') + '.'
	return mensaje

#Existing API resources.
endpoints = {
	'globales': globales,
	'pais': pais,
	'provincia': provincia
}


def interpret_watson_response(resp):
	print(resp)
	#Obtains Watsons text value from response.
	text = resp['output']['generic'][0]['text']
	entity = 'globales'
	lugar = None
	fecha = None

	#Determines whether or not Watsons response calls for API usage.	
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
		#Calls necesary API for sending message to user.
		response = endpoints[entity](intent, lugar, fecha)
		return response

	if 'Contacto' in text:
		#Watson recognizes users intent is Contact Information.
		provincia = resp['output']['entities'][0]['value'] 
		print(provincia)
		return mensaje_contacto(provincia)

	if 'Fecha' in text:
		#Cases by Date provided in MM-DD format.
		pais = resp["context"]["skills"]["main skill"]["user_defined"]['pais']
		fecha = resp["context"]["skills"]["main skill"]["user_defined"]['fecha']
		intencion = resp["context"]["skills"]["main skill"]["user_defined"]['intencion']
		print(intencion, pais, fecha)
		return endpoints['pais'](intencion, pais, fecha)

	#No API call was needed, return Watsons text value.
	return text