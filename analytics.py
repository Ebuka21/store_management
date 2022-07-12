'''
This script will perform analytics on the information from the database and display to a frontend screen for Administrative view
'''

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
from db_interact import pg_db

db = pg_db()
db.pg_connect('connect')

data = db.view()

sm_data = pd.DataFrame(data, columns=['productname','quantity','categorykey'])

print(sm_data.head())

plt.barh(sm_data['productname'],sm_data['quantity'])
plt.xlabel('Product')
plt.ylabel('Quantity')
plt.show()

