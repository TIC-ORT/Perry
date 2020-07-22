from twilio.rest import Client
import ssl
#Disables https for twilio.
https_context = ssl._create_unverified_context

def sendToNum(text=None, media=None, num=None):
	account_sid = 'AC740bb3cfc9eb3057a0e2ecc8a5bf4102' 
	auth_token = '2e931d24ac33eab0b2714c86f9036b50' 
	client = Client(account_sid, auth_token) 
	client.messages.create( 
													from_='whatsapp:+14155238886',  
													body=text,      
													media_url=media,
													to=num 
												) 
