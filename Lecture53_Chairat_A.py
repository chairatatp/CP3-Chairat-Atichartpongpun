def VatCal(total):
    result = total+(total*7/100)
    return result

print(VatCal(int(input("Your Price : "))))