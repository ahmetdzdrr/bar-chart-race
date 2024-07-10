# Stock Prices Bar Chart Race

This repository contains a project that visualizes stock prices using a bar chart race animation. The project utilizes the `bar_chart_race` library to create an engaging and dynamic visualization of monthly closing prices of selected stocks over a specified period.

## Table of Contents

- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Download Stock Data](#download-stock-data)
  - [Process the Data](#process-the-data)
  - [Create Bar Chart Race](#create-bar-chart-race)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

- `bcr.ipynb`: Jupyter Notebook containing the code for downloading stock data, processing it, and creating the bar chart race animation.
- `README.md`: This file, providing an overview of the project and instructions for use.

## Requirements

To run this project, you need to have the following libraries installed:

- `yfinance`
- `pandas`
- `bar_chart_race`
- `matplotlib`

You can install these libraries using pip:

    pip install -r requirements.txt

## Usage

1. Download Stock Data
   
The code in the notebook downloads stock data for three selected tickers (e.g., AAPL, MSFT, GOOGL) for the years 2012-2024 using the yfinance library.


        import yfinance as yf
        from datetime import datetime
        tickers = ['AAPL', 'NVDA', 'GOOGL', 'TSLA']
        data = yf.download(tickers, start='2012-01-01', end=datetime.now())

2. Process the Data

The downloaded data is processed to calculate the monthly closing prices for each stock.

        df_combined = data['Adj Close'].resample('M').last()
        df_combined = df_combined.reset_index()
        df_combined['Year'] = df_combined['Date'].dt.year
        df_combined['Month'] = df_combined['Date'].dt.month
        df_combined = df_combined.groupby(["Year", "Month"])[['AAPL', 'MSFT', 'GOOGL']].last().reset_index()

3. Create Bar Chart Race
   
The processed data is used to create a bar chart race animation using the bar_chart_race library.

        import bar_chart_race as bcr
        bcr.bar_chart_race(
            df=df_monthly,
            filename='stock_prices_race.mp4',
            title='AAPL & NVDIA & GOOGL & TSLA 2020 - 2024 Monthly Close Price History')



https://github.com/ahmetdzdrr/bar-chart-race/assets/117534684/556d6db9-a8ed-463f-84f6-13b862c6db2c



## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
