import gspread
from google.oauth2.service_account import Credentials
from config import SERVICE_ACCOUNT_FILE, SCOPES, SPREADSHEET_ID  # Импортируем нужные переменные

# 3. Авторизуемся
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(credentials)

# 4. ОТКРЫТЬ ТАБЛИЦУ (выберите ОДИН из трех способов ниже)
spreadsheet = client.open_by_key(SPREADSHEET_ID)

# 5. Выберите ЛИСТ для работы
# Способ А: Взять первый лист по умолчанию
worksheet = spreadsheet.sheet1

# Покажем первые несколько строк с листа
all_values = worksheet.get_all_values()  # Получаем все данные как список списков
print('\nПервые строки таблицы:')
for row in all_values[:5]:  # Выводим первые 5 строк
    print(row)