from tkinter import *
from tkinter import ttk
import yfinance
from currency_converter import CurrencyConverter
from datetime import date
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import requests

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
        date=date(selected_year, selected_month, selected_date)
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

def get_stock_price(ticker_symbol, api):
    url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    price = response['price'][:-3]
    return price

def get_stock_quote(ticker_symbol, api):
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    return response

def fetch_stock_data():
    stock_name = stock_entry.get()
    ticker = stock_name
    api_key = "2915f00a46c24d5ab715bca975f994b6"

    stock_data = get_stock_quote(ticker, api_key)
    stock_price = get_stock_price(ticker, api_key)

    # Display the information in the Text widget
    result_text.delete("1.0", END)
    result_text.insert(END, f"{stock_data['name']} - {stock_price}")

def show_announcement():
    announcement_text = """This program run under free plan
limited version of Twelve Data

*********************************
delay 15 min with Twelve Data
---------------------------------
800 API credits per day
8 WS credits
API key
Spreadsheets
International trial symbols
Historical data
US market data
Forex
Cryptocurrencies
Reference data
Technical indicators
Basic fundamentals
----------------------------------

plot_stock_chart from yahoo finance

*********************************

Upgrade to a premium plan to unlock all Twelve Data tools 
and the full power of our service"""
    
    # Display the announcement in the Text widget
    result_text.delete("1.0", END)
    result_text.insert(END, announcement_text)


def plot_stock_chart():
    stock_symbol = stock_entry.get()
    fetch_data = yfinance.Ticker(stock_symbol)
    hist = fetch_data.history(period='1y')

    hist['diff'] = hist['Close'] - hist['Open']
    hist.loc[hist['diff'] >= 0, 'color'] = 'green'
    hist.loc[hist['diff'] < 0, 'color'] = 'red'

    fig3 = make_subplots(specs=[[{"secondary_y": True}]])
    fig3.add_trace(go.Candlestick(x=hist.index,
                                  open=hist['Open'],
                                  high=hist['High'],
                                  low=hist['Low'],
                                  close=hist['Close'],
                                  name='Price'))
    fig3.add_trace(go.Scatter(x=hist.index, y=hist['Close'].rolling(window=20).mean(), marker_color='blue', name='20 Day MA'))
    fig3.add_trace(go.Bar(x=hist.index, y=hist['Volume'], name='Volume', marker={'color': hist['color']}), secondary_y=True)
    fig3.update_yaxes(range=[0, 700000000], secondary_y=True)
    fig3.update_yaxes(visible=False, secondary_y=True)
    fig3.update_layout(xaxis_rangeslider_visible=False)  # hide range slider
    fig3.update_layout(title={'text': f'{stock_symbol} Stock', 'x': 0.5})
    fig3.show()

    fig3.update_xaxes(rangebreaks=[
        dict(bounds=['sat', 'mon']),  # hide weekends
        dict(values=["2021-12-25", "2022-01-01"])  # hide Xmas and New Year
    ])
    fig3.write_html(f'C:\\Users\\jay\\Desktop\\PythonInOffice\\plotly_stock_chart\\{stock_symbol}_graph.html')


# GUI setup
main_window = Tk()
main_window.title("Currency Converter")

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

# New botton stock delay 15 min stock
label_stock = Label(main_window, text="Stock Name:")
label_stock.grid(row=11, column=0, padx=10, pady=10)

stock_entry = Entry(main_window)
stock_entry.grid(row=11, column=1, padx=10, pady=10)

fetch_button = Button(main_window, text="Fetch Stock Data", command=fetch_stock_data)
fetch_button.grid(row=12, column=0, columnspan=2, pady=10)

announcement_button = ttk.Button(main_window, text="Announcement", command=show_announcement)
announcement_button.grid(row=13, column=0, columnspan=2, pady=10)

result_text = Text(main_window, height=10, width=40)
result_text.grid(row=14, column=0, columnspan=2, pady=10)

# New botton for stock chart

plot_button = ttk.Button(main_window, text="Plot Stock Chart", command=plot_stock_chart)
plot_button.grid(row=15, column=0, columnspan=2, pady=10)

main_window.mainloop()
