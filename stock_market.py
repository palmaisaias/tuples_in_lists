#Problem Statement: You have been provided with stock market data, where each data point is a tuple containing a company's stock symbol, 
#--the date, and the closing price. Your task is to write a function to find the average closing price of a specified stock.

import colorama
from colorama import Back, Fore, Style
colorama.init
colorama.init(autoreset=True)

stock_data = [  #added more data to test more scenarios
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("GOOGL", "2021-01-01", 1728.0),
    ("GOOGL", "2021-01-02", 1745.0),
    ("AMZN", "2021-01-01", 3200.0),
    ("AMZN", "2021-01-02", 3215.0),
    ("TSLA", "2021-01-01", 705.0),
    ("TSLA", "2021-01-02", 718.0),
    ("FB", "2021-01-01", 268.0),
    ("FB", "2021-01-02", 270.0),
    ("NFLX", "2021-01-01", 540.0),
    ("NFLX", "2021-01-02", 545.0),
    ("IBM", "2021-01-01", 125.0),
    ("IBM", "2021-01-02", 127.0),
]

def stock_avg(stock_data):
    while True:
        print()
        closing_price = 0
        days = 0
        print(Style.BRIGHT + '        FinalFigures App')
        print('Average Closing Price Calculator')
        print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
        print()
        ticker = input('Enter the stock ticker or "exit" to quit: ').upper().strip()    #converst to uppercase to match a real ticker display
        print()
        if ticker == 'EXIT':
            print(' Thank you for using' + Style.BRIGHT + Fore.CYAN + ' FinalFigures')
            print()
            break
        for d in stock_data:    #for every element in the list stock_data
            if ticker == d[0]:  #if the input for ticker is in the 0 index
                closing_price += d[2]   #take the 2 index, which is where the price of the stock sits, and add it to var closing_price
                days += 1   #thinking of it now I may have been able to use .count()...possibly
                print()
        if days == 0: # a 0 count here means that there have been no occurances of the ticker in the data provided since a +1 is added to nd everytime ticker is found. Efficiently prevents ZeroDiv error
            print(f'    {Style.BRIGHT + Fore.RED + ticker} stock not in the data provided')
        else:
            print(f'The average closing price for {Style.BRIGHT + Fore.CYAN + ticker + Style.RESET_ALL} in the span of {Style.BRIGHT + Fore.CYAN +str(days) + Style.RESET_ALL} day(s) is {Style.BRIGHT + str(closing_price / days)}')
        print()
        


stock_avg(stock_data)