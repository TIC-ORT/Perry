import requests
from bs4 import BeautifulSoup
import csv
import io
import difflib

class API_Provincia:
	
	correciones = {
		'Buenos Aires C': 'la Ciudad Autonoma de Buenos Aires',
		'Buenos Aires P': 'Buenos Aires'
	}

	data = {}
	endpoints = ['infectados', 'fallecidos', 'recuperados']
	provincia = ''
	informacion = ''

	def __init__(self, prov=None):
		
		self.provincia = prov

	def loadAllData(self):

		url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/Argentina_medical_cases_by_province"

		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		noise = soup.find_all('td', attrs={'style':'padding:0px 2px;'})

		for td in noise:
			td.decompose()

		noise = soup.find_all('img')
		for img in noise:
			img.decompose()
		noise = soup.find_all('a')
		for a in noise:
			a.decompose()

		table = soup.find("table", class_="wikitable")
		trs = table.find_all('tr', class_="")

		html_table = '<table><tbody>'
		for tr in trs:
			html_table += str(tr)
		html_table += '</tbody></table>'

		soup = BeautifulSoup(html_table, 'html.parser')
		indexes = ['Provincia', 'infectados', 'fallecidos', 'recuperados']
		resultados = []
		for table_num, table in enumerate(soup.find_all('table')):
			for tr in table.find_all('tr'):
				row = [''.join(cell.stripped_strings) for cell in tr.find_all(['td', 'th'])]
				resultados.append(row[1:])
		#resultados = resultados[1:]

		for row in resultados:
			provKey = row[0].replace(' ', '-').replace('(', '').replace(')', '')
			self.data[provKey] = {
						indexes[1]: row[1],
						indexes[2]: row[2],
						indexes[3]: row[3]
					}

	def __str__(self):
		return self.provincia

	def get(self, info=None, prov=None):

		if prov:
			self.provincia = prov

		if len(self.data.keys()) == 0:
			self.loadAllData()

		try:
			self.provincia = difflib.get_close_matches(self.provincia, self.data.keys())[0]
		except:
			self.provincia = self.provincia
		if info:
			try:
				self.informacion = difflib.get_close_matches(info, self.endpoints)[0]
			except:
				self.informacion = self.informacion

		if info:
			return self.data[self.provincia][self.informacion]
		else:
			return self.data[self.provincia]