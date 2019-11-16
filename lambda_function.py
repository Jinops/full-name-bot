import os
import json
import requests
from private import incoming_webhook_url
from gspread_sheet import get_searched_result

message = "Lorem Ipsum JGQ and WLD is blabla"

def lambda_handler(event, context):
	# TODO implement
	text = '\n'.join(get_searched_result(message))
	payloads = {
		"attachments" : [{
			"text" : text,
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

def test():
	lambda_handler(test, test)
	update_checker()

test()
