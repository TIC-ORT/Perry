from flask import Flask, request
from assistant import *
from threading import Thread
import codecs

def run():
  app.run(host='0.0.0.0',port=8081)

def keep_alive():  
    t = Thread(target=run)
    t.start()

app = Flask(__name__)
@app.route('/')
def main():
	file = codecs.open("index.html", "r", "utf-8")
	return file.read()
  #return "200"

@app.route('/input', methods=['GET'])
def input():
	msg = request.args.get('msg')
	try:
		response = sendToAssistant(msg)
	except:
		response = "Lo sentimos hubo un error al procesar tu mensaje, intenta refrasearlo."

	try:
		#print(json.dumps(response, indent=2))
		return response['output']['generic'][0]['text']
		#return response['output']['intents'][0]['intent'] + ": " +  response['output']['generic'][0]['text']
	except:
		try:
			#print(json.dumps(response, indent=2))
			return response['output']['generic'][0]['text']
		except:
			return "Lo sentimos hubo un error al procesar tu mensaje, intenta refrasearlo."

if __name__ == '__main__':
  keep_alive()
  #run()