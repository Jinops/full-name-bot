import os
import json
import requests
from private import *

def lambda_handler(event, context):
	# TODO implement

	payloads = {
		"attachments" : [{
			"text" : "[JGQ] 1. Jungle Quests",
			"color" : "#3d0040",
		}]
	}
	post_message(incoming_webhook_url, payloads)



def post_message(url, payloads):

	response = requests.post(url, json.dumps(payloads))
	if response.status_code == 200:
		print("success")
	else :
		print("%s error" %response.status_code)


#FOR TEST
lambda_handler("TEST", "TEST")
