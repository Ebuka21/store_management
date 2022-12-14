'''
script will interact with the db (PostgreSQL in particular). Making the necessary changes and retriving information from it
'''
import psycopg2
import pandas as pd
from datetime import datetime


class pg_db:

    def __init__(self):
        self.link = ''
        self.cur = ''

    #function will enable connection to database and close it as well
    def pg_connect(self,status):

        #global link 
        
        if status == 'connect':
            self.link = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="@Ebuka79")
            self.cur = self.link.cursor()

        elif status == 'close':
            self.cur.close()
            self.link.close()
            print('connection closed')
            
        else:
            stat = input('status code incorrect please select either connect or stop: ')
            self.pg_connect(stat)


    #quick test run function to ensure that there is connection to DB
    def test_run(self):
        self.cur.execute('SELECT version()')
        print(self.cur.fetchone())

    
    def procedure(self,pk,amount):
        #this function will execute the stored procedure/function within the database
        self.cur.execute(f'CALL product_update({pk},{amount})')
    

    def view(self,view):
        #this function will return a view created in the database
        self.cur.execute(f'REFRESH MATERIALIZED VIEW {view};')
        self.cur.execute(f'SELECT * FROM {view}')
        info = self.cur.fetchall()
        return info
    

    def run_query(self,query):
        #this function will run any query passed into it and return the output
        self.cur.execute(query)
        return self.cur.fetchall()
    

    def insert_purchase(self,purchase):
        #this function will add the purchase made to the database table

        format1 ='%Y-%m-%d'

        date = datetime.date(datetime.now())
        
        for x in purchase:
            item = x
            quantity = purchase[x]['amount']
            category = purchase[x]['category']
            price = purchase[x]['price']
            key = purchase[x]['key']

            query = f"""
            INSERT INTO test_purchase(product,quantity,pk)
            VALUES('{item}',{quantity},{key})
            """
            #self.procedure(key)
            
            self.cur.execute(query)

            self.link.commit()

            print('it is done')
    

    def stock_check(self,key,count):
        #this function will check the store and confirm if the item is available or exists
        query = f"""
        SELECT quantity
        FROM product
        WHERE productkey = {key}
        """
        self.cur.execute(query)
        amount = self.cur.fetchone()
        print(amount[0])

        if count <= amount[0]:
            return 0
        else:
            return 1

    
