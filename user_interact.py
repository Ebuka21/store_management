"""
User class: Interaction with customer concerning what they want to purchase and the amount
"""

class user_class:

    def __init__(self, purchased={}):
        
    #def stock_price_number(self):
        self.stock_count = {
                'Egg':1000,
                'Indomie':1000,
                'Bread':500,
                'Butter':1000,
                'Milk':1000,
                'Sugar':1000,
                'Salt':1000,
                'Spagetti':1000,
                'Chin-chin':2000,
                'Biscuit':2000,
                'Chair':50,
                'Kettle':50,
                'Iron':50,
                'Blender':50,
                'Rechargeable fan':25,
                'Fan': 25,
                'Extension':50,
                'Table': 25,
                'Shirt':100,
                'Polo shirt':100,
                'Trousers':100,
                'Chinos':100,
                'Skirt':100,
                'Jeans':100,
                'Blouse':100
            }

        self.productkey = {
            1:'Egg',
            2:'Indomie',
            3:'Bread',
            4:'Butter',
            5:'Milk',
            6:'Sugar',
            7:'Salt',
            8:'Spagetti',
            9:'Chin-chin',
            10:'Biscuit',
            11:'Chair',
            12:'Kettle',
            13:'Iron',
            14:'Blender',
            15:'Rechargeable Fan',
            16:'Fan',
            17:'Extension',
            18:'Table',
            19:'Shirt',
            20:'Polo shirt',
            21:'Trousers',
            22:'Chinos',
            23:'Skirt',
            24:'Jeans',
            25:'Blouse'
        }

        self.stock_price = {
            'food':{
                'Egg':90,
                'Indomie':100,
                'Bread':500,
                'Butter':400,
                'Milk':1400,
                'Sugar':200,
                'Salt':200,
                'Spagetti':400,
                'Chin-chin':100,
                'Biscuit':1000
            },
            'household':{
                'Chair':15000,
                'Kettle':3000,
                'Iron':400,
                'Blender':12000,
                'Rechargeable fan':23000,
                'Fan': 15000,
                'Extension':800,
                'Table': 20000
            },
            'clothes':{
                'Shirt':2000,
                'Polo shirt':4000,
                'Trousers':5000,
                'Chinos':5000,
                'Skirt':4000,
                'Jeans':7000,
                'Blouse':7000
            }
        }

        self.purchased = purchased
        #self.food_list = [ 'Egg','Indomie','Bread','Butter','Milk','Sugar','Salt','Spagetti','Chin-chin','Biscuit']
        #self.household_list = ['Chair','Kettle','Iron','Blender','Rechargeable Fan','Extension','Table']
        #self.cloth

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
        item = int(input("What would you like to buy, select an item number: "))
        amount = int(input("How many: "))
        item_name = self.productkey[item]
        check = self.pre_check(item_name,amount)

        if check == 0:
            #check if the item has been purchased before
            if item not in self.purchased:
                self.purchased[item_name] = {}
                self.purchased[item_name]['amount'] = amount
            #if it has been purchased already then simply increase the amount purchased by the number customer provides
            elif item  in self.purchased:
                self.purchased[item_name]['amount'] += amount
        
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