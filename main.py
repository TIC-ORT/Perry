#Server dependencies
from gevent.pywsgi import WSGIServer
from threading import Thread
from flask import Flask, request, send_from_directory, redirect
from flask_mobility import Mobility
from flask_talisman import Talisman
import os

from perry_libs.usage import *

#Apis used
from perry_libs.assistant import sendToAssistant
from perry_libs.whatsapp import sendToNum
from perry_libs.new_apis import interpret_watson_response

#File management
from bs4 import BeautifulSoup
import codecs
import re
import logging
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

#Logging configuration set to debug on history.log file
logging.basicConfig(filename='misc/history.log', level=logging.DEBUG)
logging.basicConfig(
    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

date = datetime.today().strftime('%Y-%m-%d')

def run():
    #Flask built in deploy for development (lazy loading)
    #app.run(host='0.0.0.0',port=8081)

    #WSGIServer deploy for production.
    WSGIServer(('', 8081), app).serve_forever()


#Force cache reload on client
def cacheWorkaround(file):
    return file.read().replace('REPLACE', '')#date)


#Open html files
def loadPage(src):
    return codecs.open("web/"+src, "r", "utf-8")


#Designated thread for server proccess
def keep_alive():
    t = Thread(target=run)
    t.start()


#Flask app
app = Flask(__name__)
Mobility(app)
#Talisman(app, content_security_policy=None)

#Disable unneeded dependencies logging
werkzeugLog = logging.getLogger('werkzeug')
werkzeugLog.disabled = True
requestsLog = logging.getLogger("urllib3.connectionpool")
requestsLog.disabled = True

@app.route('/')
def main():
    #print(request.user_agent)
    #Main endpoint corresponds to index.html website on mobile, full website on desktop
    if request.MOBILE:
        file = loadPage("index.html")
    else:
        file = loadPage("chatbot.html")

    #Adds current date to .css and .js sources
    try:
        return cacheWorkaround(file)
    except:
        return file

@app.route('/stats')
def stats():
	return html_stats(request.MOBILE)

@app.route('/info')
def info():
    logging.info('main: ' + str(request.user_agent))
    #Info endpoint corresponds to info.html website on mobile, full website on desktop
    if request.MOBILE:
        file = loadPage("info.html")
    else:
        #file = loadPage("chatbot.html")
        return redirect('/')

    #Adds current date to .css and .js sources
    try:
        return cacheWorkaround(file)
    except:
        return file


@app.route('/demo')
def demo():
    logging.info('main: ' + str(request.user_agent))
    #Demo endpoint points to index.html website
    file = loadPage("index.html")

    #Adds current date to .css and .js sources for cache reloading
    try:
        return cacheWorkaround(file)
    except:
        return file


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon')

@app.route('/service-worker.js')
def service_worker():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'service-worker.js',
        mimetype='application/javascript')

@app.route('/.well-known/assetlinks.json')
def assetlinks():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'assetlinks.json',
        mimetype='application/json')


def removeHTML(response):
    return re.sub(
        r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))",
        '',
        BeautifulSoup(response, 'html.parser').text)


@app.route('/input', methods=['GET'])
@app.route('/demo/input', methods=['GET'])
def web():
    #server endpoint for client-watson connection
    msg = request.args.get('msg')
    if '\n' in msg:
        msg = msg.replace('\n', '')
    logging.info('Incoming: ' + msg)
    logging.info('From: ' + str(request.user_agent))
    session_id = ''
    try:
        #sends input to watson for message analize
        response, session_id = sendToAssistant(msg)
        logging.info('Watson: ' + str(response))
        try:
            #Interprets watson response, decides whether or not API calls are needed.
            response = interpret_watson_response(response)
            print(response)
        except Exception as e:
            logging.warning('Error: ' + str(e))
            response = "Lo sentimos hubo un error al procesar tu mensaje, intenta refrasearlo."
    except:
        #Critical error, either watsons response was uncall for, or server error.
        response = "Lo sentimos hubo un error al procesar tu mensaje, intenta refrasearlo."

    if session_id == 0:
        #for zero context, third party client, response is plain text.
        response = removeHTML(response)
    else:
        response = str(response) + '|' + session_id
    logging.info('Out: ' + response)
    return response


@app.route('/siri', methods=['HEAD'])
@app.route('/siri', methods=['GET'])
def siri():
    #endpoint for siri shortcut
    msg = request.args.get('msg')
    if '\n' in msg:
        msg = msg.replace('\n', '')
    logging.info('Incoming-SIRI: ' + msg)
    logging.info('From: ' + str(request.user_agent))
    session_id = ''
    try:
        #sends input to watson for message analize
        response, session_id = sendToAssistant(msg)
        logging.info('Watson: ' + str(response))
        try:
            #Interprets watson response, decides whether or not API calls are needed.
            response = interpret_watson_response(response)
        
        except Exception as e:
            logging.warning('Error: ' + str(e))
            response = "Lo sentimos hubo un error al procesar tu mensaje, intenta refrasearlo."
    except:
        response = "Lo sentimos hubo un error al procesar tu mensaje, intenta refrasearlo."
    #siri responses are stripped of both html tags and urls for propper response display
    response = removeHTML(response)
    response = str(response) + '|' + str(session_id)
    logging.info('Out: ' + response)
    print(response)
    return response

"""
@app.route('/siri', methods=['HEAD'])
def siri_head():
    response = Response()
    response.headers.add('content-length', "Perry")
    return response
"""

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    #Endpoint for whatsapp client.
    user_num = request.form['From']

    message_body = request.form['Body']

    #sends input to watson for message analize.
    response, session_id = sendToAssistant(message_body + '|')
    #session_id is not use in this client, therefore context is not available.
    #Interprets watson response, decides whether or not API calls are needed.
    response = interpret_watson_response(response)
    #Messages to be sent to whatsapp client are stripped of html tags, but unlike siris responses, contain urls for media content and information.
    response = BeautifulSoup(response, 'html.parser').text

    if '\n' in response:
        #Splits watsons response into multiple lines
        for text in response.split('\n'):
            if 'http' in text and 'gif' not in text:
                #Media content, except for gifs
                sendToNum(media=response, num=user_num)
            else:
                #Regular text message
                sendToNum(text=text, num=user_num)
    else:
        if 'http' in response and 'gif' not in response:
            #Media content, except for gifs
            sendToNum(media=response, num=user_num)
        else:
            #Regular text message
            sendToNum(text=response, num=user_num)

    return response

if __name__ == '__main__':
    keep_alive()
