from os import environ
from auxilary import validate_dates

# Date in format 'DD.MM.YYYY'
START_DATE = '01.04.2023'
FINAL_DATE = '30.04.2023'
validate_dates(START_DATE, FINAL_DATE)
DATES = START_DATE + '-' + FINAL_DATE
CODES_PATH = f'./data/{DATES}/codes/'
USERNAME = environ['username']
PASSWORD = environ['password']
URL_LOGIN = 'https://rep.mariinsky.ru/Account/Login'