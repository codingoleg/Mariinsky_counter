from constants import BALLET, EXTRAS, PERFS, REHS, MEN, WOMEN
from parser import Driver, User

if __name__ == '__main__':
    # Login via webdriver and collect all codes
    Driver().get_all_codes()

    user = User()
    # Parse through events to get json
    for event_type in (BALLET, EXTRAS):
        for action_type in (PERFS, REHS):
            user.run_parser(event_type, action_type)
        # Aggregate and convert json to csv. Write csv to xls
        for gender in (MEN, WOMEN):
            user.aggregate_to_csv(event_type, gender)
            user.write_to_xls(event_type, gender)
