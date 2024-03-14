systemMenu = {"ข้าวหมกไก่":45,"ข้าวมันไก่":40,"ข้าวมันไก่ทอด":45,"ข้าวมันไก่ผสม":50}
menuList = []

def ShowBills():
    print("My food".center(21,"-"))
    total = 0
    for n in range(len(menuList)):
        total += int(menuList[n][1])
        print(menuList[n][0],menuList[n][1])
    print("Total Price(THB):",total)

while True:
    menuName = input("Please enter menu: ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

ShowBills()