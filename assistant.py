import ssl
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
https_context = ssl._create_unverified_context

def sendToAssistant(textInput):
	assistant_apiKey = 'AecJ5YF082OlogBDuauxmWe7rJJydKOeLVDHvT4NRb4P'
	assistant_url = 'https://api.us-south.assistant.watson.cloud.ibm.com/instances/2275fed5-c9f1-4540-82ff-1d76ad82140c'
	assistant_id = 'b2fe84b0-b3a6-48f0-b531-10a089b0beb9'

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

	return response