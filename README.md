# fx_tracking_project

fx_tracking_project is a partial automated tool for getting exchange rates between some currencies. And writing output as CSV using pandas.

The currency list is, 
AUD
CAD
CHF
DKK
EUR
GBP
HKD
IDR
INR
JPY
MXN
SEK
SGD
THB
USD
VND

## Running

Before running, implement two things.
  - Install the requirements.txt.
  - update exchangeratesapi credential(API_KEY) in settings.py, currently not included in the code, because mentioned in project description.

Goto the correct directory, and use below command for running.

```bash
python exchange_query_ops.py
```

## Results

For refering the results, Please go to the current date folder and open the "exchange_rates_out.csv" file.

## Remarks

This project includes 3 main files,

- exchange_query_ops.py: This contains main handling function for different currencies.
- utils.py: This includes all functions such as, url generator, request module and CSV writer.
- settings.py: This includes comon values and settings.
