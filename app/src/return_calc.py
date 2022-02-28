from src.Classes.Portfolio import portfolio
from src.Classes.Stocks import stock

def avg_by_portfolio(portfolios):
        avg_by_portfolio = {}
        for portfolio in portfolios:
            average = avg_return(portfolio.Stocks)
            if avg_by_portfolio.get(portfolio.ID) is None:
                avg_by_portfolio[portfolio.ID] = average
        return avg_by_portfolio


def avg_return(stocks):
        if len(stocks) == 0:
            total_return = 0
        for stock in stocks:
            total_return = total_return + stock.rate_of_return
        return total_return / len(stocks)
