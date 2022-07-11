# IMPORTS
import requests
import pandas as pd
from pathlib import Path
from settings import *

# main currency lists
currency_list = ["AUD", "CAD", "CHF", "DKK", "EUR", "GBP", "HKD", "IDR", "INR", "JPY", "MXN", "SEK", "SGD", "THB", "USD", "VND"]

def create_api_url(currency):
    '''
    creating API URL for exchange rates request
    '''

    currency_list.remove(currency)
    api_url = 'https://api.apilayer.com/exchangerates_data/latest?base=' + currency + '&symbols=' + ','.join(currency_list)
    currency_list.append(currency)
    
    return api_url

def parse_requests(api_url):
    '''
    request module for exchange rates requests
    '''

    counter = 0
    while True:
        final_response = ''
        if counter <= 3:
            try:
                final_response = requests.get(api_url, headers=headers)
                if final_response and final_response.status_code == 200:
                    break
                elif final_response.status_code == 404:
                    break
            except:
                pass
        else:
            final_response = ''
            break
    
    return final_response

def write_to_csv(api_response):
    '''
    process request response and write to CSV
    '''

    response_json = api_response.json()
    success = response_json.get('success')

    if success:
        base = response_json.get('base')
        date = response_json.get('date')

        rates = response_json.get('rates')
        for key, value in rates.items():
            csv_data['currency_from'].append(base)
            csv_data['currency_to'].append(key)
            csv_data['exchange_rate'].append(value)

        # write to csv using pandas
        df = pd.DataFrame(csv_data)
        filepath = Path(date + '/exchange_rates_out.csv')
        filepath.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(filepath)

        check = True

    else:
        check = False

    return check
