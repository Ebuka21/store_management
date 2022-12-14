'''
This script will perform analytics on the information from the database and display to a frontend screen for Administrative view
'''

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
from db_interact import pg_db

def bar_plot(x,y,orient,colors=[]):
    if orient == 'h':
        plot = plt.barh(x,y,color=colors)
    else:
        plot = plt.barh(x,y,color=colors)

    plt.bar_label(plot, padding=3)

def stock_analysis(data):
    #separating the full stock information into different categories
    food_stock = data[data['categorykey']==1]
    house_stock = data[data['categorykey']==2]
    cloth_stock = data[data['categorykey']==3]


    #fig,ax = plt.subplots(figsize = (20,10))
    plt.figure(figsize=(20,20))

    plt.subplot(2,2,1)
    colors = ["red" if i <= 30 else "blue" for i in food_stock['quantity'] ]
    bar_plot(food_stock['productname'],food_stock['quantity'],'h',colors)
    plt.ylabel('Product')
    plt.xlabel('Quantity')

    plt.subplot(2,2,2)
    colors = ["red" if i <= 5 else "blue" for i in house_stock['quantity'] ]
    bar_plot(house_stock['productname'],house_stock['quantity'],'h',colors)
    plt.ylabel('Product')
    plt.xlabel('Quantity')

    plt.subplot(2,2,3)
    colors = ["red" if i <= 5 else "blue" for i in cloth_stock['quantity'] ]
    bar_plot(cloth_stock['productname'],cloth_stock['quantity'],'h',colors)
    plt.ylabel('Product')
    plt.xlabel('Quantity')


    plt.show()


def purchase_analysis(data):
    
    pass

db = pg_db()
db.pg_connect('connect')


#retrieve information on the stock
stock = db.view('test1_view')
purchase = db.view('test2_view')

#transform output from database into pandas dataframe
stock_data = pd.DataFrame(stock, columns=['productname','quantity','categorykey'])
purchase_data = pd.DataFrame(purchase, columns=['productkey','date','product','quantity','price','total','categorykey'])

stock_analysis(stock_data)

'''
#separating the full stock information into different categories
food_stock = stock_data[stock_data['categorykey']==1]
house_stock = stock_data[stock_data['categorykey']==2]
cloth_stock = stock_data[stock_data['categorykey']==3]


#fig,ax = plt.subplots(figsize = (20,10))
plt.figure(figsize=(20,20))

plt.subplot(2,2,1)
colors = ["red" if i <= 30 else "blue" for i in food_stock['quantity'] ]
bar_plot(food_stock['productname'],food_stock['quantity'],'h',colors)
#nd = plt.barh(food_stock['productname'],food_stock['quantity'],color=colors)
#plt.bar_label(nd, padding=3)
plt.ylabel('Product')
plt.xlabel('Quantity')

plt.subplot(2,2,2)
colors = ["red" if i <= 5 else "blue" for i in house_stock['quantity'] ]
bar_plot(house_stock['productname'],house_stock['quantity'],'h',colors)
#nd = plt.barh(house_stock['productname'],house_stock['quantity'],color=colors)
p#lt.bar_label(nd, padding=3)
plt.ylabel('Product')
plt.xlabel('Quantity')

plt.subplot(2,2,3)
colors = ["red" if i <= 5 else "blue" for i in cloth_stock['quantity'] ]
bar_plot(cloth_stock['productname'],cloth_stock['quantity'],'h',colors)
#nd = plt.barh(cloth_stock['productname'],cloth_stock['quantity'],color=colors)
#plt.bar_label(nd, padding=3)
plt.ylabel('Product')
plt.xlabel('Quantity')


plt.show()
'''

    

    

