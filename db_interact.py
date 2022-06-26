'''
script will interact with the db. Making the necessary changes and retriving information from it
'''
import psycopg2
import pandas as pd

class pg_db:

    def __init__(self):
        self.link = ''
        self.cur = ''

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

    def test_run(self):
        
        self.cur.execute('SELECT version()')
        print(self.cur.fetchone())

        retrieve_com = """
        SELECT * 
        FROM category
        """

        self.cur.execute(retrieve_com)
        print('new sql query')
        print(self.cur.fetchall())
        
        self.pg_connect('close')

    def insert_purchase(self):
        #this function will add the purchase made to the database table
        pass
    
    def stock_check(self):
        #this function will check the store and confirm if the item is available or exists
        pass

    def procedure(self):
        #this function will execute the stored procedure/function within the database
        pass
    
    def view(self):
        #this function will return a view created in the database
        pass
