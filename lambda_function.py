import os
import json
import requests
from private import *
from gspread_sheet import get_searched_result

message = "Lorem Ipsum JGQ and WLD is blabla"

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


def test():
	print(*sorted(get_searched_result(message)), sep='\n')

test()
