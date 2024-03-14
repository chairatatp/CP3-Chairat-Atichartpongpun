menuList = []
priceList = []

def ShowBills():
    print("My food".center(21,"-"))
    total = 0
    for n in range(len(menuList)):
        total += int(priceList[n])
        print(menuList[n].capitalize(),priceList[n])
    print("Total Price(THB):", total)

while True:
    menuName = input("Please enter menu: ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price: ")
        menuList.append(menuName)
        priceList.append(menuPrice)

ShowBills()