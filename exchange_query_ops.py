# IMPORTS
from utils import *
from settings import *

# main currency lists
currency_list = ["AUD", "CAD", "CHF", "DKK", "EUR", "GBP", "HKD", "IDR", "INR", "JPY", "MXN", "SEK", "SGD", "THB", "USD", "VND"]

def exchange_query():
    '''
    main handling function for exchange rates query
    '''

    for currency in currency_list:
        # create URL for request
        api_url = create_api_url(currency)

        # request with URL
        api_response = parse_requests(api_url)

        if api_response and api_response.status_code == 200:
            # write to CSV
            check = write_to_csv(api_response)

            if check:
                print ('**************** Got exchange rates for currency %s and saved in CSV *****************' %  (currency))

            else:
                print ('**************** Missed exchange rates for currency %s *****************' %  (currency))

        else:
            print ('********************* Got Request Error with currency %s **************************' % (currency))

    print ('\n************* Completed the processing, please refer the CSV file saved in current date folder for rates ***************')

exchange_query()
