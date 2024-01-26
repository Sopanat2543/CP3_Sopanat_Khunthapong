from tkinter import *
from tkinter import ttk
from currency_converter import CurrencyConverter
from datetime import date

def left_click_button_1(event):
    c = CurrencyConverter()
    conversion_result = c.convert(
        text_box_amount.get(),
        combobox_currency_1.get(),
        combobox_currency_2.get()
    )
    label_result_1.configure(text=f"Result: {conversion_result}")

def left_click_button_2(event):
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

main_window.mainloop()
