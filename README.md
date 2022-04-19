# store_management

<p>
This project involves interation done at a store and managing it. Several actions will be done with the combination of Python, PostgreSQL and Analysis
</p>

<ol>
<li> <b>PostgreSQL</b> - This will store all the data for the store including the inventory, price, customer information</li>
<li> <b>Python</b> - All functions and interactions will be scripted using python as well as a connection to the database to update it continuously</li>
<li> <b>Analysis</b> - With the use of pandas, mathplotlib and django/flask, the summary of the days purchase and other analysis will be displayed</li>
</ol>
### Functions created and their purpose

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

<li>user_interact</li>
<li>user_purchase</li>
<li>update_stock</li>
<li>check_store</li>
<li>pre_check_store</li>
<li>user_int</li>
<li>pre_check_s</li>