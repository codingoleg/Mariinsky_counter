from constants import MEN, WOMEN
from parser import Driver, User, Data, BALLET, EXTRAS, PERFS, REHS

if __name__ == '__main__':
    # Login via webdriver and collect all codes
    Driver().get_all_codes()

    user = User()
    data = Data()
    # Parse through events to get json
    for event_type in (BALLET, EXTRAS):

        for action_type in (PERFS, REHS):
            user.run_parser(event_type, action_type)

        # Aggregate and convert json to csv. Write csv to xls
        for gender in (MEN, WOMEN):
            data.aggregate_to_csv(event_type, gender)
            data.write_to_xls(event_type, gender)
