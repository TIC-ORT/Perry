from twilio.rest import Client
import ssl
#Disables https for twilio.
https_context = ssl._create_unverified_context
import os

def sendToNum(text=None, media=None, num=None):

	account_sid = os.getenv("account_sid")
	auth_token = os.getenv("auth_token")

	client = Client(account_sid, auth_token) 
	client.messages.create( 
													from_='whatsapp:+14155238886',  
													body=text,      
													media_url=media,
													to=num 
												) 
