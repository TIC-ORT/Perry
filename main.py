from flask import Flask, request, send_from_directory
import os
from assistant import *
from threading import Thread
import codecs
import warnings
warnings.filterwarnings("ignore")
from gevent.pywsgi import WSGIServer
from Provincia import API_Provincia
import json
from whatsapp import sendToNum                         
from datetime import datetime
from bs4 import BeautifulSoup
import re
import logging
logging.basicConfig(filename='history.log',level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

date = datetime.today().strftime('%Y-%m-%d')

def run():
  app.run(host='0.0.0.0',port=8081)
	#WSGIServer(('', 8081), app).serve_forever()

def keep_alive():  
    t = Thread(target=run)
    t.start()

app = Flask(__name__)

werkzeugLog = logging.getLogger('werkzeug')
werkzeugLog.disabled = True
requestsLog = logging.getLogger("urllib3.connectionpool")
requestsLog.disabled = True

@app.route('/')
def main():
	file = codecs.open("index.html", "r", "utf-8")
	return file.read().replace('REPLACE', date)

@app.route('/info')
def info():
	file = codecs.open("info.html", "r", "utf-8")
	return file.read().replace('REPLACE', date)

@app.route('/test')
def test():
	file = codecs.open("test.html", "r", "utf-8")
	return file.read().replace('REPLACE', date)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/input', methods=['GET'])
def web():
	msg = request.args.get('msg')
	logging.info('Incoming: '+msg)
	session_id = ''
	try:
		response, session_id = sendToAssistant(msg)
		logging.info('Watson: '+str(response))
		try:
			response = interpret_watson_response(response)
			print(response)
		except Exception as e:
			logging.warning('Error: '+str(e))
			response = "Lo sentimos hubo un error al procesar tu mensaje, intenta refrasearlo."
	except:
		response = "Lo sentimos hubo un error al procesar tu mensaje, intenta refrasearlo."
    
	if session_id == 0:
		response = re.sub(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", '', BeautifulSoup(response, 'html.parser').text)
	else:
		response =  str(response)+'|'+session_id
	logging.info('Out: '+response)
	return response 

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
	user_num = request.form['From']

	message_body = request.form['Body']

	response, session_id = sendToAssistant(message_body+'|')
	response = interpret_watson_response(response)
	response = re.sub(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", '', BeautifulSoup(response, 'html.parser').text)
	
	if '\n' in response:
		for text in response.split('\n'):
			if 'http' in response: 
				sendToNum(media=response, num=user_num)
			else:
				sendToNum(text=text, num=user_num)
	else:
		if 'http' in response and 'gif' not in response: 
			sendToNum(media=response, num=user_num)
		else:
			sendToNum(text=response, num=user_num)

	return response

"""
@app.route('/test', methods=['GET'])
def test():
	msg = request.args.get('msg')
	try:
		response = sendToAssistant(msg)
	except:
		response = "Lo sentimos hubo un error al procesar tu mensaje, intenta refrasearlo."
	return response+'\s'+session_id
"""

@app.route('/api/provincia/<string:prov>/<string:info>/', methods=['GET'])
@app.route('/api/provincia/<string:prov>/', methods=['GET'])
def api(prov=None, info=None):
	api = API_Provincia(prov)
	if info is None:
		jsonOutput = 	{	
										"status": "success",
										'data':{
												prov: api.get()
											}
									}
		return json.dumps(jsonOutput, ensure_ascii=False)

	number = api.get(info)
	jsonOutput = 	{	
									"status": "success",
									'data':{
										'Provincia':prov,
										info:int(number.replace(',', ''))
									}
								}
	return json.dumps(jsonOutput, ensure_ascii=False)

@app.route('/api/provincias/')
def endpoints():
	api = API_Provincia()
	api.loadAllData()
	jsonOutput = 	{	
									"status": "success",
									'data':{
										'Provincias':list(api.data.keys())
										}
								}
	return json.dumps(jsonOutput, ensure_ascii=False)


if __name__ == '__main__':

  keep_alive()
  #http_server = WSGIServer(('', 8081), app)
  #http_server.serve_forever()
	#WSGIServer(('', 8081), app).serve_forever()
  #run()