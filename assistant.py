import ssl
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
https_context = ssl._create_unverified_context
from new_apis import *

def sendToAssistant(textInput):
	assistant_apiKey = '_iyBvcIwxxiX5nZ5blCqXIvH9RxdAzjs491C2zKMKd1k'
	assistant_url = 'https://api.us-south.assistant.watson.cloud.ibm.com/instances/4b7c9dbf-8744-42f2-8601-ad43a3eb0490'
	assistant_id = 'fe2e4610-8398-44fe-add6-0408f549e784'

	authenticator = IAMAuthenticator(assistant_apiKey)
	assistant = AssistantV2(
	    version='2020-02-05',
	    authenticator=authenticator
	)

	assistant.set_service_url(assistant_url)

	assistant.set_disable_ssl_verification(True)

	session_id = assistant.create_session(
	    assistant_id=assistant_id
	).get_result()['session_id']


	response = assistant.message(
	    assistant_id=assistant_id,
	    session_id=session_id,
	    input={
	        'message_type': 'text',
	        'text': textInput
	    }
	).get_result()
	
	response = interpret_watson_response(response)

	return response