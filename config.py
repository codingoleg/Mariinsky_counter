from os import environ
from utils import validate_dates

# Account
USERNAME = environ['username']
PASSWORD = environ['password']
URL_LOGIN = environ['url_login']
URL_EVENT = environ['url_event']

# Dates
start_date = '01.08.2023'
final_date = '31.08.2023'
validate_dates(start_date, final_date)
dates = start_date + '-' + final_date

# Paths
codes_path = f'./data/{dates}/codes/'
json_path = f'./data/{dates}/json/'
csv_path = f'./data/{dates}/csv/'
xls_path = f'./data/{dates}/xls/'
workbook_path = './templates/excel/template.xlsx'

# Event types
BALLET = 'ballet'
EXTRAS = 'extras'

# Participation types
FEAT = 'feat'
SECURE = 'secure'

# Action types
PERFS = 'perfs'
REHS = 'rehs'

# Gender
MEN = 'men'
WOMEN = 'women'

# For TQDM
bar_format = '{desc}:|{bar}|{percentage:3.0f}% {n_fmt}/{total_fmt} [{elapsed}]'