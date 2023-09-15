from config import DATES

# Paths
CODES_PATH = f'./data/{DATES}/codes/'
JSON_PATH = f'./data/{DATES}/json/'
CSV_PATH = f'./data/{DATES}/csv/'
XLS_PATH = f'./data/{DATES}/xls/'
WORKBOOK_PATH = './templates/excel/template.xlsx'

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
BAR_FORMAT = '{desc}:|{bar}|{percentage:3.0f}% {n_fmt}/{total_fmt} [{elapsed}]'