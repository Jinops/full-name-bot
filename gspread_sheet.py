import gspread
from private import permission_json_file, sheet_url, sheet_name

#authorize
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(permission_json_file, scope)
gc = gspread.authorize(credentials)
doc = gc.open_by_url(sheet_url)
worksheet = doc.worksheet(sheet_name)

def get_searched_result(find_title):
	#parse data
	find_title_head = "SS/"
	cell = worksheet.find(find_title_head + find_title)
	gameID = worksheet.cell(cell.row,cell.col-3).value
	gameName = worksheet.cell(cell.row,cell.col-1).value
	
	return ("%s. %s" %(gameID, gameName))


