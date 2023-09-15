from os import environ
from utils import validate_dates

# Account
USERNAME = environ['username']
PASSWORD = environ['password']
URL_LOGIN = environ['url_login']
URL_EVENT = environ['url_event']

# Dates
START_DATE = '01.08.2023'
FINAL_DATE = '31.08.2023'
validate_dates(START_DATE, FINAL_DATE)
DATES = START_DATE + '-' + FINAL_DATE
