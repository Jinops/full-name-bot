import os
import json

def lambda_handler(event, context):
	# TODO implement
    incoming_webhook_url = get_json()
    print (incoming_webhook_url)

def get_json():
	with open("private.json") as json_file:
		# Sample of private.json 
		# {"url" : "https://www.google.co.kr"}
		json_data = json.load(json_file)
		return json_data["url"]

#FOR TEST
lambda_handler("TEST", "TEST")
