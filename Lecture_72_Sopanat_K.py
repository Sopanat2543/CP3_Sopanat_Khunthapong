menuList = []

def showBill():
    print("---- My Food----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        totalPrice += int(menuList[number][1])
    print("Total :", totalPrice)
while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])
showBill()  
