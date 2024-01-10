def vatCalculate(totalPrice):
    result = totalPrice + totalPrice * 7/100
    return result

totalPrice = int(input("Enter total price: "))

result = vatCalculate(totalPrice)
print("Total price with VAT:", result)

    