"""Contains all the indicators used in the dataset building process
"""

# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Define Classes
class CrossMovingAverageIndicator:
    """Generates Indication when to buy and sell based on moving
    averages
    """
    def __init__(self, data, column):
        self.data_for_analysis = data
        self.column_of_interest = column
        self.sma_short = self.get_simple_moving_avg(self.data_for_analysis, 'Close')
        self.sma_long = self.get_simple_moving_avg(self.data_for_analysis, 'Close', 100)
        self.indicators = self.calculate_trade_decisions(self.sma_short, self.sma_long)

    def get_simple_moving_avg(self, data, column, window_for_avg=30):
        """Gets the simple moving average

        Args:
            data (Yf data struct): Data from yf
            column (string): Column of interest
            window_for_avg (int, optional): window to average over. Defaults to 30.

        Returns:
            Data Column: simple moving average
        """
        return data[column].rolling(window=window_for_avg).mean()

    def calculate_trade_decisions(self, long_term_sma, short_term_sma):
        """Signals when to buy and sell baseed on the two columns

        Args:
            long_term_sma (Data Column): long term moving average
            short_term_sma (data Column): short term moving average
        """
        # Initialise decisions
        stock_decision = []
        # Set flag (0 = holding, 1 = buy, 2 = sell)
        flag = 0

        for i in range(len(long_term_sma)):
            # If short term has crossed above long term
            if short_term_sma[i] > long_term_sma[i]:
                # Check we have not already bought
                if flag != 1:
                    # Buy if not already bought
                    stock_decision.append(1)
                    flag = 1
                else:
                    # Hold
                    stock_decision.append(0)
            elif short_term_sma[i] < long_term_sma[i]:
                # Check if we have sold
                if flag != 2:
                    # Sell if sold
                    stock_decision.append(2)
                    flag = 2
                else:
                    # Hold
                    stock_decision.append(0)
            else:
                # Hold
                stock_decision.append(0)
        return stock_decision

    def visualise_indicator_strategy(self):
        """Visualises the generated indicator performance
        """
        # Define the indicator section
        buy_scatter = []
        sell_scatter = []

        for i in range(len(self.data_for_analysis)):
            if self.indicators[i] == 0:
                buy_scatter.append(np.nan)
                sell_scatter.append(np.nan)
            elif self.indicators[i] == 1:
                buy_scatter.append(self.data_for_analysis[self.column_of_interest][i])
                sell_scatter.append(np.nan)
            else:
                buy_scatter.append(np.nan)
                sell_scatter.append(self.data_for_analysis[self.column_of_interest][i])

        plt.figure(figsize=(12.6, 4.6))
        plt.plot(self.data_for_analysis[self.column_of_interest], label=self.column_of_interest)
        plt.plot(self.sma_short, label="SMA30")
        plt.plot(self.sma_long, label="SMA100")
        plt.scatter(self.data_for_analysis.index, buy_scatter, label="Buy", marker="^", color='green')
        plt.scatter(self.data_for_analysis.index, sell_scatter, label='Sell', marker="*", color='red')
        plt.show()
        
        