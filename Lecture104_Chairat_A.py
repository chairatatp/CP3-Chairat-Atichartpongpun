class customer:
    firstname = ""
    lastname = ""
    age = 0

    def addcart(self):
        print("Added product to",self.firstname,self.lastname,"'s card")

customer1 = customer()
customer1.firstname = "Chairat"
customer1.lastname = "Atp"
customer1.addcart()

customer2 = customer()
customer2.firstname = "Cc"
customer2.lastname = "Atp"
customer2.addcart()

customer3 = customer()
customer3.firstname = "Bjr"
customer3.lastname = "Atp"
customer3.addcart()

customer4 = customer()
customer4.firstname = "Kmw"
customer4.lastname = "Atp"
customer4.addcart()