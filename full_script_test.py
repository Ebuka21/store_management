from user_interact import user_class
from db_interact import pg_db


test =  user_class()

test.main()

'''
test1 = pg_db()
test1.pg_connect('connect')
test1.test_run()
purchase = {'Indomie': {'amount': 40, 'category': 'food', 'price': 2000},'chin-chin': {'amount': 40, 'category': 'food', 'price': 2000}}
test1.insert_purchase(purchase)
test1.stock_check(4,5)
test1.pg_connect('close')
'''