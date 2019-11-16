import os
import json
from gspread_sheet import save_sheet
from datetime import datetime

live_time = datetime.today()
sheet = []


def search():
	global sheet
	#is_time_passed(datetime.now(), datetime.timedelta(days=30))
	#if (datetime.today() )
	sheet = load_json()
	last_updated_time = sheet[0]
	print(last_updated_time)
	#	save_sheet()


def update_checker():
	sprint (live_time)

def load_json():
	if not os.path.exists("sheet.json"):
		save_sheet(live_time.strftime("%Y-%m-%d"))
		
	with open('sheet.json') as json_file:
		sheet_json = json.load(json_file)
	return sheet_json


#def is_time_passed(live_time, period):



search()