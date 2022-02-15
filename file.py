import codecademylib3
import pandas as pd

#reading the csv with pd
inventory = pd.read_csv("inventory.csv")
#showing the first 10 rows
staten_island = inventory.head(10)

#picking a column
product_request = staten_island["product_description"]
#print(product_request)

#logic to request rows fulfling certain requirements
seed_request = inventory[\
(inventory.location =="Brooklyn")\
& (inventory.product_type == "seeds")]
#print(seed_request)

#Adding a column to inventory
#if the lambda function proves to be true 
inventory["in_stock"] = inventory.quantity.apply(lambda x: True\
if x > 0\
else False )
#print(inventory.in_stock)

#New column called total_value where price * quantity 
inventory["total_value"] = inventory.price * inventory.quantity
#print(inventory)

#lambda function combining columns 
combine_lambda = lambda row:'{} - {}'.format(row.product_type, row.product_description)

inventory["full_description"] = inventory.apply(combine_lambda, axis =1)
print(inventory)


