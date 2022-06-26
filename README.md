# store_management

<p>
This project involves interation done at a store and managing it. Several actions will be done with the combination of Python, PostgreSQL and Analysis
</p>

<ol>
<li> <b>PostgreSQL</b> - This will store all the data for the store including the inventory, price, customer information</li>
<li> <b>Python</b> - All functions and interactions will be scripted using python as well as a connection to the database to update it continuously</li>
<li> <b>Analysis</b> - With the use of pandas, mathplotlib and django/flask, the summary of the days purchase and other analysis will be displayed</li>
<li> <b>Django</b> - this will be the web interface for showcasing the statistics of the store; can later be implemented to be the web interface for purchasing the items</li>
</ol>

### <u>Functions created and their purpose</u>

#### Auto purchase

<li>
rd_purchase - this will produce the number of purchases that will be done that day (limit:10)
</li>

<li>
item_purchase - this function returns a list of items that will be purchased picked at random
</li>

<li>
final_price - this function will the produce the number bought for each of the items
</li>

<li>
item_limit_purchase - adjusted function which will take into consideration the limit set for each item to be purchased
</li>

<li>
new_item_purchase - this function will be able to detect the category of the item purchased and record it alongside other information
</li>

#### User input

<li>
user_int - function obtain what the customer wants to purchase and saves the information to a dictionary
</li>

<li>
pre_check - in the process of the customer making a purchase, this checks if the item is still available
</li>

<li>
user_purchase - this uses the customers input to compute the total price of an item purchased and obtain what category the item falls under
</li>

<li>
update_stock - this will update the stock dictionary based on what has been purchased
</li>

<li>
check_store - this checks the stock dictionary and triggers if the amount certain items are below 5 or 10 so it can be restocked
</li>

### <u>Database Tables</u>

<ol>category</ol>
<t><li>categorykey</li></t>

<ol>product</ol>
<t></t>


