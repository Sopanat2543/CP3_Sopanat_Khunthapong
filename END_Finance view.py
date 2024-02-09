from tkinter import *
import tkinter as tk
from tkinter import ttk, Text
import yfinance as yf 
from currency_converter import CurrencyConverter
import datetime 
import datetime as date
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import requests
import pytz

def left_click_button_1(event): # Convert current currency value
    c = CurrencyConverter()
    conversion_result = c.convert(
        text_box_amount.get(),
        combobox_currency_1.get(),
        combobox_currency_2.get()
    )
    label_result_1.configure(text=f"Result: {conversion_result}")

def left_click_button_2(event): # Compare currency values
    selected_year = int(combobox_year.get())
    selected_month = int(combobox_month.get())
    selected_date = int(combobox_date.get())

    c = CurrencyConverter()
    conversion_result = c.convert(
        text_box_amount.get(),
        combobox_currency_1.get(),
        combobox_currency_2.get(),
        date=datetime.datetime(selected_year, selected_month, selected_date)
    )
    label_result_2.configure(text=f"Result: {conversion_result}")

def compare_graph(): # Create a graph of the data from label_result_1 and label_result_2
    result_1 = label_result_1.cget("text").split(": ")[1]
    result_2 = label_result_2.cget("text").split(": ")[1]

    try:
        result_1 = float(result_1)
        result_2 = float(result_2)

        labels = ['To Day', 'Selected Time']
        values = [result_1, result_2]

        plt.bar(labels, values)
        plt.ylabel('Amount')
        plt.title('Comparison of Conversion Results')
        plt.show()

    except ValueError:
        print("Results are not valid numeric values.")
    
def show_announcement():
    announcement_text = """

***********************************************
This program run under data from yahoo finance
----------------------------------------------

International trial symbols
Historical data
US market data
Forex
Reference data
Technical indicators
Basic fundamentals

For Cryptocurrencies
name-USD
Ex BTC-USD

-----------------------------------------------

plot_stock_chart from yahoo finance

***********************************************

"""
    
    # Display the announcement in the Text widget
    result_text.delete("1.0", END)
    result_text.insert(END, announcement_text)

def fetch_stock_data():
    stock = stock_entry.get()
    time_period = time_period_combobox.get()

    recent_data = yf.download(stock, period=time_period)
    result_text.delete("1.0", END)
    result_text.insert(END, recent_data)

def more_info():
    stock = stock_entry.get().upper()  # Get stock name from Entry and convert to uppercase
    GetInformation = yf.Ticker(stock)
    select = select_combobox.get()  # Get selected info from Combobox

    select_options = ['address1', 'city', 'state', 'zip', 'country', 'phone', 'website', 'industry', 'industryKey',
                    'industryDisp', 'sector', 'sectorKey', 'sectorDisp', 'longBusinessSummary', 'fullTimeEmployees',
                    'companyOfficers', 'fiscalYear', 'exercisedValue', 'unexercisedValue',
                    'auditRisk', 'boardRisk', 'compensationRisk', 'shareHolderRightsRisk', 'overallRisk', 'governanceEpochDate', 
                    'compensationAsOfEpochDate', 'maxAge', 'priceHint', 'previousClose', 'open', 'dayLow', 'dayHigh', 
                    'regularMarketPreviousClose', 'regularMarketOpen', 'regularMarketDayLow', 'regularMarketDayHigh', 'dividendRate', 
                    'dividendYield', 'exDividendDate', 'payoutRatio', 'fiveYearAvgDividendYield', 'beta', 'trailingPE', 'forwardPE', 
                    'volume', 'regularMarketVolume', 'averageVolume', 'averageVolume10days', 'averageDailyVolume10Day', 'bid', 'ask', 
                    'bidSize', 'askSize', 'marketCap', 'fiftyTwoWeekLow', 'fiftyTwoWeekHigh', 'priceToSalesTrailing12Months', 'fiftyDayAverage', 
                    'twoHundredDayAverage', 'trailingAnnualDividendRate', 'trailingAnnualDividendYield', 'currency', 'enterpriseValue', 'profitMargins', 
                    'floatShares', 'sharesOutstanding', 'sharesShort', 'sharesShortPriorMonth', 'sharesShortPreviousMonthDate', 'dateShortInterest', 
                    'sharesPercentSharesOut', 'heldPercentInsiders', 'heldPercentInstitutions', 'shortRatio', 'shortPercentOfFloat', 'impliedSharesOutstanding', 
                    'bookValue', 'priceToBook', 'lastFiscalYearEnd', 'nextFiscalYearEnd', 'mostRecentQuarter', 'earningsQuarterlyGrowth', 'netIncomeToCommon', 
                    'trailingEps', 'forwardEps', 'pegRatio', 'lastSplitFactor', 'lastSplitDate', 'enterpriseToRevenue', 'enterpriseToEbitda', '52WeekChange', 
                    'SandP52WeekChange', 'lastDividendValue', 'lastDividendDate', 'exchange', 'quoteType', 'symbol', 'underlyingSymbol', 'shortName', 'longName', 
                    'firstTradeDateEpochUtc', 'timeZoneFullName', 'timeZoneShortName', 'uuid', 'messageBoardId', 'gmtOffSetMilliseconds', 'currentPrice', 'targetHighPrice', 
                    'targetLowPrice', 'targetMeanPrice', 'targetMedianPrice', 'recommendationMean', 'recommendationKey', 'numberOfAnalystOpinions', 'totalCash', 
                    'totalCashPerShare', 'ebitda', 'totalDebt', 'quickRatio', 'currentRatio', 'totalRevenue', 'debtToEquity', 'revenuePerShare', 'returnOnAssets', 
                    'returnOnEquity', 'freeCashflow', 'operatingCashflow', 'earningsGrowth', 'revenueGrowth', 'grossMargins', 'ebitdaMargins', 'operatingMargins', 
                    'financialCurrency', 'trailingPegRatio']  

    if select in select_options:
        if select in ['governanceEpochDate', 'compensationAsOfEpochDate', 'exDividendDate',
                      'sharesShortPreviousMonthDate','maxAge', 'dateShortInterest', 'lastFiscalYearEnd',
                      'nextFiscalYearEnd', 'mostRecentQuarter', 'lastSplitDate', 'lastDividendDate',
                      'firstTradeDateEpochUtc']:
            # Get the value from the dictionary
            select_epoch = GetInformation.info[select]

            # Convert UNIX epoch time to local time
            date_utc = datetime.datetime.utcfromtimestamp(select_epoch)
            local_timezone = pytz.timezone('Asia/Bangkok')
            date_local = date_utc.replace(tzinfo=pytz.utc).astimezone(local_timezone)

            result_text.delete(1.0, tk.END)  # Clear previous text
            result_text.insert(tk.END, f"{select} (Local Time): {date_local}")
        else:
            result_text.delete(1.0, tk.END)  # Clear previous text
            result_text.insert(tk.END, f"{select}: {GetInformation.info[select]}")
    else:
        result_text.delete(1.0, tk.END)  # Clear previous text
        result_text.insert(tk.END, "Invalid selection. Please choose from the available options.")

def plot_stock_chart():
    stock_symbol = stock_entry.get()
    time = time_period_combobox.get()
    fetch_data = yf.Ticker(stock_symbol)
    hist = fetch_data.history(period=time)

    hist['diff'] = hist['Close'] - hist['Open']
    hist.loc[hist['diff'] >= 0, 'color'] = 'green'
    hist.loc[hist['diff'] < 0, 'color'] = 'red'

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Candlestick(x=hist.index,
                                  open=hist['Open'],
                                  high=hist['High'],
                                  low=hist['Low'],
                                  close=hist['Close'],
                                  name='Price'))
    fig.add_trace(go.Scatter(x=hist.index, y=hist['Close'].rolling(window=20).mean(), marker_color='blue', name='20 Day MA'))
    fig.add_trace(go.Bar(x=hist.index, y=hist['Volume'], name='Volume', marker={'color': hist['color']}), secondary_y=True)
    fig.update_yaxes(range=[0, 700000000], secondary_y=True)
    fig.update_yaxes(visible=False, secondary_y=True)
    fig.update_layout(xaxis_rangeslider_visible=False)  # ซ่อนตัวเลื่อนช่วง
    fig.update_layout(title={'text': f'{stock_symbol} Stock', 'x': 0.5})

    # ตั้งตำแหน่งของแกน x
    fig.update_xaxes(rangebreaks=[
        dict(bounds=['sat', 'mon']),  # ซ่อนวันเสาร์และวันอาทิตย์
        dict(values=["2023-12-25", "2024-01-01"])  # ซ่อนวันคริสต์มาสและวันปีใหม่
    ])
    
    # แสดงกราฟ
    fig.show()

    # เขียนไฟล์ HTML
    fig.write_html(f'C:\\Users\\jay\\Desktop\\PythonInOffice\\plotly_stock_chart\\{stock_symbol}_graph.html')

# GUI setup
main_window = Tk()
main_window.title("Finance view")

# Currency Converter GUI
label_currency_1 = Label(main_window, text="From Currency:")
label_currency_1.grid(row=0, column=0)
currency_codes = ['EUR', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HUF', 'RON',
                   'MYR', 'SEK', 'SGD', 'HKD', 'AUD', 'CHF', 'KRW', 'CNY', 'TRY', 'HRK',
                   'NZD', 'THB', 'USD', 'NOK', 'RUB', 'INR', 'MXN', 'CZK', 'BRL', 'PLN',
                   'PHP', 'ZAR']
combobox_currency_1 = ttk.Combobox(main_window, values=currency_codes)
combobox_currency_1.grid(row=0, column=1)

label_currency_2 = Label(main_window, text="To Currency:")
label_currency_2.grid(row=1, column=0)
combobox_currency_2 = ttk.Combobox(main_window, values=currency_codes)
combobox_currency_2.grid(row=1, column=1)

label_amount = Label(main_window, text="Amount:")
label_amount.grid(row=2, column=0)
text_box_amount = Entry(main_window)
text_box_amount.grid(row=2, column=1)

calculate_button_1 = Button(main_window, text="Calculate Direct Conversion")
calculate_button_1.bind('<Button-1>', left_click_button_1)
calculate_button_1.grid(row=3, column=1)
label_result_1 = Label(main_window, text="")
label_result_1.grid(row=3, column=2)

# Currency Value Comparison GUI
label_title_2 = Label(main_window, text="Compare Currency Value by Date")
label_title_2.grid(row=5, column=0)

label_year = Label(main_window, text="Year:")
label_year.grid(row=6, column=0)
years = [str(2000 + i) for i in range(201)]
combobox_year = ttk.Combobox(main_window, values=years)
combobox_year.grid(row=6, column=1)

label_month = Label(main_window, text="Month:")
label_month.grid(row=7, column=0)
months = [str(i).zfill(2) for i in range(1, 13)]
combobox_month = ttk.Combobox(main_window, values=months)
combobox_month.grid(row=7, column=1)

label_date = Label(main_window, text="Date:")
label_date.grid(row=8, column=0)
dates = [str(i).zfill(2) for i in range(1, 32)]
combobox_date = ttk.Combobox(main_window, values=dates)
combobox_date.grid(row=8, column=1)

calculate_button_2 = Button(main_window, text="Calculate Conversion by Date")
calculate_button_2.bind('<Button-1>', left_click_button_2)
calculate_button_2.grid(row=9, column=1)
label_result_2 = Label(main_window, text="")
label_result_2.grid(row=9, column=2)

# New button for comparing results Graph
compare_button = Button(main_window, text="Compare Results (Graph)", command=compare_graph)
compare_button.grid(row=10, column=1, pady=10)


# New botton stock
label_stock = Label(main_window, text="Stock Name:")
label_stock.grid(row=11, column=0, padx=10, pady=10)

stock_entry = Entry(main_window)
stock_entry.grid(row=11, column=1, padx=10, pady=10)

# Time period selection
label_time = Label(main_window, text="Time period:")
label_time.grid(row=15, column=0, padx=10, pady=10)
time_periods = ['30s', '1min', '5min', '10min', '30min', '1h', '3h', '5h', '1d', '1w', '1mo', '1y', 'ytd', '5y', '10y', 'max']
time_period_combobox = ttk.Combobox(main_window, values=time_periods)
time_period_combobox.grid(row=15, column=1, padx=10, pady=10)

# Button to fetch data
fetch_button = Button(main_window, text="Fetch Data", command=fetch_stock_data)
fetch_button.grid(row=11, column=2, columnspan=2, pady=10)


# Select info Combobox
select_label = ttk.Label(main_window, text="Select info:")
select_label.grid(row=12, column=0, padx=5, pady=5, )
select_options = ['address1', 'city', 'state', 'zip', 'country', 'phone', 'website', 'industry', 'industryKey',
                    'industryDisp', 'sector', 'sectorKey', 'sectorDisp', 'longBusinessSummary', 'fullTimeEmployees',
                    'companyOfficers', 'fiscalYear', 'exercisedValue', 'unexercisedValue',
                    'auditRisk', 'boardRisk', 'compensationRisk', 'shareHolderRightsRisk', 'overallRisk', 'governanceEpochDate', 
                    'compensationAsOfEpochDate', 'maxAge', 'priceHint', 'previousClose', 'open', 'dayLow', 'dayHigh', 
                    'regularMarketPreviousClose', 'regularMarketOpen', 'regularMarketDayLow', 'regularMarketDayHigh', 'dividendRate', 
                    'dividendYield', 'exDividendDate', 'payoutRatio', 'fiveYearAvgDividendYield', 'beta', 'trailingPE', 'forwardPE', 
                    'volume', 'regularMarketVolume', 'averageVolume', 'averageVolume10days', 'averageDailyVolume10Day', 'bid', 'ask', 
                    'bidSize', 'askSize', 'marketCap', 'fiftyTwoWeekLow', 'fiftyTwoWeekHigh', 'priceToSalesTrailing12Months', 'fiftyDayAverage', 
                    'twoHundredDayAverage', 'trailingAnnualDividendRate', 'trailingAnnualDividendYield', 'currency', 'enterpriseValue', 'profitMargins', 
                    'floatShares', 'sharesOutstanding', 'sharesShort', 'sharesShortPriorMonth', 'sharesShortPreviousMonthDate', 'dateShortInterest', 
                    'sharesPercentSharesOut', 'heldPercentInsiders', 'heldPercentInstitutions', 'shortRatio', 'shortPercentOfFloat', 'impliedSharesOutstanding', 
                    'bookValue', 'priceToBook', 'lastFiscalYearEnd', 'nextFiscalYearEnd', 'mostRecentQuarter', 'earningsQuarterlyGrowth', 'netIncomeToCommon', 
                    'trailingEps', 'forwardEps', 'pegRatio', 'lastSplitFactor', 'lastSplitDate', 'enterpriseToRevenue', 'enterpriseToEbitda', '52WeekChange', 
                    'SandP52WeekChange', 'lastDividendValue', 'lastDividendDate', 'exchange', 'quoteType', 'symbol', 'underlyingSymbol', 'shortName', 'longName', 
                    'firstTradeDateEpochUtc', 'timeZoneFullName', 'timeZoneShortName', 'uuid', 'messageBoardId', 'gmtOffSetMilliseconds', 'currentPrice', 'targetHighPrice', 
                    'targetLowPrice', 'targetMeanPrice', 'targetMedianPrice', 'recommendationMean', 'recommendationKey', 'numberOfAnalystOpinions', 'totalCash', 
                    'totalCashPerShare', 'ebitda', 'totalDebt', 'quickRatio', 'currentRatio', 'totalRevenue', 'debtToEquity', 'revenuePerShare', 'returnOnAssets', 
                    'returnOnEquity', 'freeCashflow', 'operatingCashflow', 'earningsGrowth', 'revenueGrowth', 'grossMargins', 'ebitdaMargins', 'operatingMargins', 
                    'financialCurrency', 'trailingPegRatio']  
select_combobox = ttk.Combobox(main_window, values=select_options)  
select_combobox.grid(row=12, column=1, padx=5, pady=5)

# Button to get more info
info_button = ttk.Button(main_window, text="Get Info", command=more_info)
info_button.grid(row=12, column=2, padx=5, pady=5)

# Button to get announcement
announcement_button = ttk.Button(main_window, text="Announcement", command=show_announcement)
announcement_button.grid(row=10, column=2, columnspan=2, pady=10)

# Text box to display result
result_text = Text(main_window, height=20, width=100)
result_text.grid(row=18, column=0, columnspan=3, padx=5, pady=5)

# New botton for stock chart

plot_button = ttk.Button(main_window, text="Plot Stock Chart", command=plot_stock_chart)
plot_button.grid(row=15, column=2, columnspan=2, pady=10)

main_window.mainloop()
