import os
import json
from gspread_sheet import save_sheet
from datetime import datetime

live_time = datetime.today()
sheet = []
update_cycle = 30 # Days


def search():
	global sheet
	load_json()
	get_all_title()

###########################
def load_json():
	global sheet
	if not os.path.exists("sheet.json"):
		save_sheet(live_time.strftime("%Y-%m-%d"))
		print("sheet is created")
	
	with open('sheet.json') as json_file:
		sheet = json.load(json_file)

	if is_update_cylce(live_time, update_cycle) :
			save_sheet(live_time.strftime("%Y-%m-%d"))
			print("sheet is updated")

def is_update_cylce(live_time, period):
	global sheet
	last_updated_time = datetime.strptime(sheet[0], "%Y-%m-%d")
	day_passed = (live_time - last_updated_time).days
	if (day_passed >= 30):
		return True
	else :
		return False
###########################


def get_all_title():
	global sheet
	all_title = []
	for title in sheet :
		all_title.append(title[4])
	print(all_title)

search()