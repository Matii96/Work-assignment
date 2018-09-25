import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('Optymalizacja pracy-18d16f9d299c.json', scope)

gc = gspread.authorize(credentials)

sheet = gc.open('Arkusz testowy').sheet1
#print(sheet.get_all_records())

pola = sheet.range('A2:D2')
for pole in pola:
    print(pole.value)
