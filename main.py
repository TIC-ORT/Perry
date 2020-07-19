from flask import Flask, request
from assistant import *
from threading import Thread
import codecs
import warnings
warnings.filterwarnings("ignore")
from gevent.pywsgi import WSGIServer
from Provincia import API_Provincia

from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')

def run():
  #app.run(host='0.0.0.0',port=8081)
	WSGIServer(('', 8081), app).serve_forever()

def keep_alive():  
    t = Thread(target=run)
    t.start()

app = Flask(__name__)
@app.route('/')
def main():
	file = codecs.open("index.html", "r", "utf-8")
	return file.read().replace('REPLACE', date)

@app.route('/input', methods=['GET'])
def input():
	msg = request.args.get('msg')
	try:
		response = sendToAssistant(msg)
	except:
		response = "Lo sentimos hubo un error al procesar tu mensaje, intenta refrasearlo."
	return response


@app.route('/<string:prov>/<string:info>/', methods=['GET'])
def api(prov, info):	
	api = API_Provincia(prov)
	number = api.get(info)
	json = {'Provincia':prov,
					info:int(number.replace(',', ''))
					}
	return json


if __name__ == '__main__':
  keep_alive()
  #http_server = WSGIServer(('', 8081), app)
  #http_server.serve_forever()
	#WSGIServer(('', 8081), app).serve_forever()
  #run()