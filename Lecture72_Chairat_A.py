menuList = []

def ShowBills():
    print("My food".center(21,"-"))
    total = 0
    for n in range(len(menuList)):
        total += int(menuList[n][1])
        print(menuList[n][0].capitalize(),menuList[n][1])
    print("Total Price(THB):", total)

while True:
    menuName = input("Please enter menu: ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price: ")
        menuList.append([menuName,menuPrice])

ShowBills()