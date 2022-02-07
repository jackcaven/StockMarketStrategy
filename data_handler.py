"""
Description
-----------
Deals with the retrieving, handling, viewing containing of all the data used to build
the datasets

Classes
------
StockData

"""

# Import libraries
import numpy as np
import pandas as pd
import matplotlib as plt
import yfinance as yf

# Define Classes
class StockData:
    """
    Description
    -----------
    Takes and holds all the data in terms of stocks

    Properties
    ----------

    Methods
    -------
    """
    def __init__(self, stock_tag):
        self.stock_tag = stock_tag
        self.stock_data_struct = self.get_data_from_tag()

    def get_data_from_tag(self):
        """Gets data from yfinance using given tag in constructor

        Returns:
            [DataStruct]: History of the stock values for analysis
        """
        return yf.Ticker(self.stock_tag).history("max")
