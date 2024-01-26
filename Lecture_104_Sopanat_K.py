class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " + self.lastName + "'s cart")

customer1 = Customer()
customer1.name = "Bob"
customer1.lastName = "Baby"
customer1.age = 8

customer2 = Customer()
customer2.name = "Billy"
customer2.lastName = "Bobbybrown"
customer2.age = 18

customer3 = Customer()
customer3.name = "Bolfish"
customer3.lastName = "Billo"
customer3.age = 81

customer4 = Customer()
customer4.name = "Badygade"
customer4.lastName = "rikarisui"
customer4.age = 800000


customer1.addCart()
customer2.addCart()
customer3.addCart()
customer4.addCart()
