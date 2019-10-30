import os
import json
import requests

def lambda_handler(event, context):
	# TODO implement

	payloads = {
		"attachments" : [{
			"text" : "[JGQ] 1. Jungle Quests",
			"color" : "#3d0040",
		}]
	}

	incoming_webhook_url = get_json()
	post_message(incoming_webhook_url, payloads)

def get_json():
	with open("private.json") as json_file:
		# Sample of private.json 
		# {"url" : "https://www.google.co.kr"}
		json_data = json.load(json_file)
		return json_data["url"]

def post_message(url, payloads):

	response = requests.post(url, json.dumps(payloads))
	if response.status_code == 200:
		print("success")
	else :
		print("%s error" %response.status_code)



#FOR TEST
lambda_handler("TEST", "TEST")
