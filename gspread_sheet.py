import gspread
from private import permission_json_file, sheet_url, sheet_name

from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(permission_json_file, scope)
gc = gspread.authorize(credentials)

doc = gc.open_by_url(sheet_url)
worksheet = doc.worksheet(sheet_name)

#colum B(2) : ID | colum D(4) : Game Name | colum E(5) : Game Title
colum_data = worksheet.col_values(5)
print(colum_data)
