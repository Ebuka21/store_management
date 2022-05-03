"""
User class: Interaction with customer concerning what they want to purchase and the amount
"""

class user_class:

    def __init__(self, purchased={}):
        
    #def stock_price_number(self):
        self.stock_count = {
                'Egg': 100,
                'Bread':100,
                'Indomie':100,
                'Butter':100,
                'Milk':100,
                'Sugar':100,
                'Chair': 10,
                'Table': 5,
                'fan': 7
            }

        self.stock_price = {
            'food':{
                'Egg': 90,
                'Bread':500,
                'Indomie':100,
                'Butter':800,
                'Milk':1400,
                'Sugar':200,
            },
            'household':{
                'Chair': 15000,
                'Table': 20000,
                'fan': 17000
            }
        }

        self.purchased = purchased
        self.food_list = [ 'Egg','Bread','Indomie','Butter','Milk','Sugar']
        self.household_list = ['Chair','Table','fan']

    def display(self):
        print(
            """
        Below are the prices of our items in stock

        Egg     --> 90
        Bread   --> 500
        Indomie --> 100
        Butter  --> 800
        Milk    --> 1400
        Sugar   --> 200
        Chair   --> 15000
        Table   --> 20000
        fan     --> 17000
        """
        )

    def pre_check(self,item, count):
        c = 0
        if item in self.stock_count and count > self.stock_count[item]:
            print("sorry we only have " + str(stock[y][item]) + " " + item + " left in stock")
            c = 1
        elif item not in self.stock_count:
            print("Sorry but we do not have this in stock")
            c = 1
        return c

    def user_int(self):
        #purchased = self.purchased
        item = input("What would you like to buy: ")
        amount = int(input("How many: "))
        check = self.pre_check(item,amount)

        if check == 0:
            #check if the item has been purchased before
            if item not in self.purchased:
                self.purchased[item] = {}
                self.purchased[item]['amount'] = amount
            #if it has been purchased already then simply increase the amount purchased by the number customer provides
            elif item  in self.purchased:
                self.purchased[item]['amount'] += amount
        
        else:
            print("returning")
            print(self.purchased)
            user_class.user_int(self)

        return self.purchased

    def user_purchase(self,purchased):
        for item in purchased:
            for category in self.stock_price:
                if item in self.stock_price[category]:
                    purchased[item]['category'] = category
                    purchased[item]['price'] = purchased[item]['amount']*self.stock_price[category][item]
        return purchased

    def update_stock(self,stock,purchase):
        #using full_stock_dict and dictionary created from purchased items
        a = stock
        b = purchase
        for x in b:
            if x in a:
                a[x] -= b[x]['amount']
                #if subtracting the amount creates a negative value then it will be normalised to zero
                if a[x] <= 0:
                    a[x] = 0
        return a

    def check_store(self,stock):
        for x in stock:
            if x in self.food_list and stock[x] <= 10:
                print("URGENT: " + x + " is low in stock")
            elif x in self.household_list and stock[x] < 5:
                print("URGENT: " + x + " is low in stock")


    def main(self):
        print("Hello Welcome esteemed customer to our store \n")

        self.display()

        print("\n")

        ask = input("Do you want to purchase anything: ")

        if ask == 'yes':
            #purchased = {}
            #loop will enable customer to continuosly state what they want to buy
            while ask:

                purchase = self.user_int()

                #cont = pre_check_store(stock_count,purchase)
                
                
                buy = self.user_purchase(purchase)
                #find out if they want to continue shopping
                ask = input("Would you like to continue shopping: ")
                if ask == 'yes':
                    continue
                else:
                    #break the loop at this point
                    ask = False
                    print(buy)
                    stock_count = self.update_stock(self.stock_count, self.purchased)
                    self.check_store(self.stock_count)
                    print("This is the new stock count: ")
                    print(self.stock_count)
                
                     
        elif ask == 'no':
            print("Thank you for visiting with us")

        else:
            print('Sorry that is a wrong input, please choose yes or no')
            self.main()