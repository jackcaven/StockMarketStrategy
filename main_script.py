"""
Title
-----
Stock Market Dataset Retriever

Description
-----------
This should take offer a list of stocks to look at and or use to build a training dataset

"""

# Import libraries
import data_handler as dh
import stock_trade_indicators as sti

# Define Classes

# Define Methods
def __main__():
    stock_data = dh.StockData("TSLA")
    indicator = sti.CrossMovingAverageIndicator(stock_data.stock_data_struct, 'Close')
    indicator.visualise_indicator_strategy()

__main__()
