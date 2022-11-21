"""
User class: Interaction with customer concerning what they want to purchase and the amount
"""
import pandas as pd
import db_interact
from db_interact import pg_db

class user_class:

    def __init__(self, purchased={}):
        stockcountquery = 'SELECT productname, quantity FROM product'
        productkeyquery = 'SELECT productkey,productname FROM product'
        foodquery = 'SELECT productname,price FROM product WHERE categorykey=1'
        householdquery = 'SELECT productname,price FROM product WHERE categorykey=2'
        clothquery = 'SELECT productname,price FROM product WHERE categorykey=3'
        
        self.db = pg_db()
        self.db.pg_connect('connect')
        
    #def stock_price_number(self):
        self.stock_count = pd.DataFrame(self.db.run_query(stockcountquery), columns=['productname','quantity'])
        self.stock_count.set_index('productname',inplace=True)
        self.stock_count = self.stock_count.to_dict()['quantity']

        self.productkey = pd.DataFrame(self.db.run_query(productkeyquery), columns=['productkey','productname'])
        self.productkey.set_index('productkey',inplace=True)
        self.productkey = self.productkey.to_dict()['productname']

        self.food = pd.DataFrame(self.db.run_query(foodquery), columns=['productname','price'])
        self.food.set_index('productname',inplace=True)
        self.food = self.food.to_dict()['price']

        self.household = pd.DataFrame(self.db.run_query(householdquery), columns=['productname','price'])
        self.household.set_index('productname',inplace=True)
        self.household = self.household.to_dict()['price']

        self.clothes = pd.DataFrame(self.db.run_query(clothquery), columns=['productname','price'])
        self.clothes.set_index('productname',inplace=True)
        self.clothes = self.clothes.to_dict()['price']


        
        self.stock_price = {
            'food':self.food,
            'household':self.household,
            'clothes':self.clothes
        }

        self.purchased = purchased


    def display(self):
        print(
            """
        Below are the prices of our items in stock

        1	Egg			        90
        2	Indomie			    100
        3	Bread			    500
        4	Butter			    400
        5	Milk			    1400
        6	Sugar			    200
        7	Salt			    200
        8	Spagetti		    400
        9	Chin-chin		    100
        10	Biscuit			    1000
        11	Chair			    15000
        12	Kettle			    3000
        13	Iron			    4000
        14	Blender			    12000
        15	Rechargeable Fan	23000
        16	Fan			        15000
        17	Extension		    800
        18	Table		    	30000
        19	Shirt			    2000
        20	Polo shirt		    4000
        21	Trousers		    5000
        22	Chinos			    5000
        23	Skirt			    4000
        24	Jeans			    7000
        25	Blouse			    7000

        """
        )

    def pre_check(self,item, count):
        #check the item
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
        key = int(input("What would you like to buy, select an item number: "))
        amount = int(input("How many: "))
        item = self.productkey[key]
        #check = self.pre_check(item,amount)
        check = self.db.stock_check(key,amount)


        if check == 0:
            #check if the item has been purchased before
            if item not in self.purchased:
                self.purchased[item] = {}
                self.purchased[item]['amount'] = amount
                self.purchased[item]['key'] = key
            #if it has been purchased already then simply increase the amount purchased by the number customer provides
            elif item in self.purchased:
                self.purchased[item]['amount'] += amount
            self.db.procedure(key,amount)
        
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
    '''
    def check_store(self,stock):
        for x in stock:
            if x in self.food_list and stock[x] <= 10:
                print("URGENT: " + x + " is low in stock")
            elif x in self.household_list and stock[x] < 5:
                print("URGENT: " + x + " is low in stock")
'''
    def check_store(self,stock):
        for x in stock:
            if stock[x] <= 10:
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
                    self.db.insert_purchase(buy)
                    print(buy)
                    stock_count = self.update_stock(self.stock_count, self.purchased)
                    self.check_store(self.stock_count)
                    print("This is the new stock count: ")
                    print(self.stock_count)
                
                     
        elif ask == 'no':
            print("Thank you for visiting with us")
            self.db.pg_connect('close')

        else:
            print('Sorry that is a wrong input, please choose yes or no')
            self.main()