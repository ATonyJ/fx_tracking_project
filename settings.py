'''
This file for settings and constant values
'''

# configuration for exchangeratesapi API requests
API_KEY = ''
headers = {
    'apikey': API_KEY
    }

# main data dict for writing CSV
csv_data = {
            'currency_from': [],
            'currency_to': [],
            'exchange_rate': []
            }
