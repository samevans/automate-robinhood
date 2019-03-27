from Robinhood import Robinhood
from pprint import pprint
import config

my_trader = Robinhood()

my_trader.login(username=config.APP_CONFIG['username'], password=config.APP_CONFIG['password'])

#Get stock information
    #Note: Sometimes more than one instrument may be returned for a given stock symbol
stock_instrument = my_trader.instruments("GEVO")[0]

#Get a stock's quote
my_trader.print_quote("AAPL")

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

for row in my_trader.positions()['results']:
    if float(row['quantity']) == 0:
        continue
    pprint(row)
    trade = my_trader.get_url(row['instrument'])
    pprint(trade)