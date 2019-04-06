from Robinhood import Robinhood
from pprint import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import config

# Auth to Robinhood
trader = Robinhood()
trader.login(username=config.ROBINHOOD_CONFIG['username'], password=config.ROBINHOOD_CONFIG['password'])

# Auth to Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('googlesheets.json', scope)
gc = gspread.authorize(credentials)

#Get stock information
    #Note: Sometimes more than one instrument may be returned for a given stock symbol
#stock_instrument = my_trader.instruments("GEVO")[0]

#Get a stock's quote
#my_trader.print_quote("AAPL")

#Prompt for a symbol
#my_trader.print_quote()

#Print multiple symbols
#my_trader.print_quotes(stocks=["BBRY", "FB", "MSFT"])

#View all data for a given stock ie. Ask price and size, bid price and size, previous close, adjusted previous close, etc.
#quote_info = my_trader.quote_data("AAPL")
#print(quote_info)


#owned_sec = ('owned_securities', my_trader.securities_owned())

#for result in owned_sec[1]['results']:
#    pprint(result)

for row in trader.positions()['results']:
    if float(row['quantity']) == 0:
        continue
    pprint(row)
    trade = trader.get_url(row['instrument'])
    pprint(trade)
    break
    
wks = gc.open("Portfolio").sheet1

print(wks)