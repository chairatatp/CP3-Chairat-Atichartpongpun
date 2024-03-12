def login():
    username = input("username : ")
    password = input("password : ")
    if username == "Name" and password == "1234":
        print("logging in")
        return show_menu()
    else:
        print("error")
        return login()
def show_menu():
    print("*****CShop*****")
    print("1.Vat Calculator")
    print("2.Price Calculator")
    return menu_select()
def menu_select():
    userselect = int(input(">>"))
    if userselect == 1:
        return vat_cal(int(input("Price (THB):")))
    elif userselect == 2:
        return price_cal()
    else:
        print("error")
        return menu_select()
def vat_cal(price):
    vat = 7
    result = price + (price * vat / 100)
    return result
def price_cal():
    price1 = int(input("First Order Price: "))
    price2 = int(input("Second Order Price: "))
    return vat_cal(price1 + price2)

print(login())