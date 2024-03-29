import gspread
import json
from private import permission_json_file, sheet_url, sheet_name

#authorize
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(permission_json_file, scope)
gc = gspread.authorize(credentials)
doc = gc.open_by_url(sheet_url)
worksheet = doc.worksheet(sheet_name)

game_title_head = "SS/" #It can be changed

def get_searched_result(message):
	return get_result_by_title(get_included_title(message))

def get_included_title(message): # Get title from sheet
	find_title = []
	game_list = get_all_title()
	del game_list[0]
	i = 0
	for game_title in game_list:
		game_title = game_title.replace(game_title_head, "")
		if game_title in message:
			find_title.append(game_title)
			i += 1
	return find_title

def get_result_by_title(titles): # Get Result from title
	result = []
	for title in titles:
		cell = worksheet.find(game_title_head + title)
		gameID = worksheet.cell(cell.row,cell.col-3).value
		gameName = worksheet.cell(cell.row,cell.col-1).value
		result.append("[%s] %s. %s" %(title, gameID, gameName))
	return result

def get_all_title():
	return worksheet.col_values(5)

def save_sheet(updated_time):
	sheet_list = []
	sheet_list = worksheet.get_all_values()
	sheet_list.insert(0, updated_time)
	with open("sheet.json", 'w', encoding='utf-8') as make_file:
		json.dump(sheet_list, make_file, indent="\t")

