import yfinance as yf
import json
import os


class StockPortfolio:
    def __init__(self, portfolio_file='portfolio.json'):
        self.portfolio_file = portfolio_file
        self.portfolio = self.load_portfolio()

    def load_portfolio(self):
        """Load the portfolio from the file."""
        if os.path.exists(self.portfolio_file):
            with open(self.portfolio_file, 'r') as file:
                return json.load(file)
        return {}

    def save_portfolio(self):
        """Save the portfolio to the file."""
        with open(self.portfolio_file, 'w') as file:
            json.dump(self.portfolio, file, indent=4)

    def add_stock(self, ticker, shares):
        """Add a stock to the portfolio."""
        if ticker in self.portfolio:
            self.portfolio[ticker]['shares'] += shares
        else:
            self.portfolio[ticker] = {'shares': shares}
        self.save_portfolio()

    def remove_stock(self, ticker, shares):
        """Remove a stock from the portfolio."""
        if ticker in self.portfolio:
            if self.portfolio[ticker]['shares'] >= shares:
                self.portfolio[ticker]['shares'] -= shares
                if self.portfolio[ticker]['shares'] == 0:
                    del self.portfolio[ticker]
                self.save_portfolio()
            else:
                print(f"Cannot remove {shares} shares, you only have {self.portfolio[ticker]['shares']} shares of {ticker}.")
        else:
            print(f"Stock {ticker} not in portfolio.")

    def get_stock_data(self, ticker):
        """Fetch real-time stock data."""
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        return data['Close'].iloc[0]  # Get the most recent closing price

    def track_portfolio(self):
        """Track the portfolio performance."""
        total_value = 0
        portfolio_summary = []

        for ticker, info in self.portfolio.items():
            current_price = self.get_stock_data(ticker)
            current_value = current_price * info['shares']
            portfolio_summary.append({
                'ticker': ticker,
                'shares': info['shares'],
                'current_price': current_price,
                'total_value': current_value
            })
            total_value += current_value

        return portfolio_summary, total_value

    def display_portfolio(self):
        """Display the portfolio summary."""
        portfolio_summary, total_value = self.track_portfolio()

        print("\nStock Portfolio Summary:")
        for stock in portfolio_summary:
            print(f"{stock['ticker']} - {stock['shares']} shares - Current Price: ${stock['current_price']:.2f} - Total Value: ${stock['total_value']:.2f}")

        print(f"\nTotal Portfolio Value: ${total_value:.2f}")


def main():
    portfolio = StockPortfolio()

    print("Welcome to the Stock Portfolio Tracker!")

    while True:
        print("\nOptions:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            ticker = input("Enter stock ticker symbol (e.g., AAPL, GOOG): ").upper()
            shares = int(input("Enter the number of shares: "))
            portfolio.add_stock(ticker, shares)
            print(f"Added {shares} shares of {ticker} to your portfolio.")
        
        elif choice == '2':
            ticker = input("Enter stock ticker symbol (e.g., AAPL, GOOG): ").upper()
            shares = int(input("Enter the number of shares to remove: "))
            portfolio.remove_stock(ticker, shares)
        
        elif choice == '3':
            portfolio.display_portfolio()
        
        elif choice == '4':
            print("Exiting the Stock Portfolio Tracker.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
