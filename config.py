from os import environ
from auxilary import validate_dates

# Date in format 'DD.MM.YYYY'
START_DATE = '01.06.2023'
FINAL_DATE = '30.06.2023'
validate_dates(START_DATE, FINAL_DATE)
DATES = START_DATE + '-' + FINAL_DATE
CODES_PATH = f'./data/{DATES}/codes/'
JSON_PATH = f'./data/{DATES}/json/'
CSV_PATH = f'./data/{DATES}/csv/'
USERNAME = environ['username']
PASSWORD = environ['password']
URL_LOGIN = environ['url_login']
URL_EVENT = environ['url_event']