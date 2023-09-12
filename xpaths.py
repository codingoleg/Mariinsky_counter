from config import BALLET


def dropdown_menu_option(ballet_extras):
    menu_code = '3' if ballet_extras == BALLET else '6'
    return f"//li[@data-original-index='{menu_code}']"


username = 'InputL'
password = 'InputP'
start_date = 'startDate'
final_date = 'finishDate'
dropdown_menu = "//div[@class='btn-group bootstrap-select']"
submit = 'submit'
links = "//a[contains(@href, '/Home/MoreInfo/')]"
