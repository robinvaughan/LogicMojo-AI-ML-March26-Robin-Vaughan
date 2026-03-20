# Question 5:- An e-commerce company exports its daily order log in the following format. 
# Each order contains multiple pieces of information:
# orders = 
    # [ ["ORD001","Laptop",75000,"Completed"],
    # ["ORD002","Mouse",500,"Completed"], 
    # ["ORD003","Laptop",75000,"Returned"], 
    # ["ORD004","Keyboard",1500,"Completed"], 
    # ["ORD005","Laptop",75000,"Completed"], 
    # ["ORD006","Monitor",20000,"Fraud"], 
    # ["ORD007","Mouse",500,"Completed"], 
    # ["ORD008","Laptop",75000,"Completed"] ]

# Each row represents an order with the following structure:
    # [Order_ID , Product_Name , Price , Status]
# Where: 
    # Order_ID → unique order identifier 
    # Product_Name → product purchased 
    # Price → price of the product 
    # Status → order status (Completed, Returned, Fraud)


# 1. Display All Orders Using a nested loop, print the entire order table row by row so that each order’s details are displayed clearly.

# headers = ["Order ID" , "Product Name" , "Price" , "Status"]
# orders = [ ["ORD001","Laptop",75000,"Completed"], ["ORD002","Mouse",500,"Completed"], ["ORD003","Laptop",75000,"Returned"], ["ORD004","Keyboard",1500,"Completed"], ["ORD005","Laptop",75000,"Completed"], ["ORD006","Monitor",20000,"Fraud"], ["ORD007","Mouse",500,"Completed"], ["ORD008","Laptop",75000,"Completed"] ]
# print("~" * 60) # Separator line
# print(f"{headers[0]:<15}{headers[1]:<15}{headers[2]:<15}{headers[3]:<15}")
# print("~" * 60) # Separator line
# for index, order in enumerate(orders):
#     print(f"{order[0]:<15}{order[1]:<15}{order[2]:<15}{order[3]:<15}")
#     print("-" * 60) # Separator line


# 2. Detect Suspicious Activity The system suspects fraud when: the same product appears more than 3 times, OR an order has status "Fraud"
# orders = [ ["ORD001","Laptop",75000,"Completed"], ["ORD002","Mouse",500,"Completed"], ["ORD003","Laptop",75000,"Returned"], ["ORD004","Keyboard",1500,"Completed"], ["ORD005","Laptop",75000,"Completed"], ["ORD006","Monitor",20000,"Fraud"], ["ORD007","Mouse",500,"Completed"], ["ORD008","Laptop",75000,"Completed"] ]
# remove_duplicate = list()
# for index, order in enumerate(orders):
#     product_name = order[1]
#     count = 0
#     for i in range(len(orders)):
#         if (orders[i][1] == product_name):
#             count += 1

#     if(count>3 and product_name not in remove_duplicate):
#         print(f"The Order with Product name: '{order[1]}' appeared {count} so its suspicious")
#         remove_duplicate.append(product_name)
    
    
#     if (order[3] == 'Fraud'):
#         print(f"The Order with Order ID: '{order[0]}' and Product name: '{order[1]}' was found to be '{order[3]}'")
    
# 3. Calculate Total Revenue Only Completed orders contribute to revenue. 
# Write code that: iterates through the dataset adds the price of all completed orders prints the total revenue generated for the day.
# total_revenue = 0
# orders = [ ["ORD001","Laptop",75000,"Completed"], ["ORD002","Mouse",500,"Completed"], ["ORD003","Laptop",75000,"Returned"], ["ORD004","Keyboard",1500,"Completed"], ["ORD005","Laptop",75000,"Completed"], ["ORD006","Monitor",20000,"Fraud"], ["ORD007","Mouse",500,"Completed"], ["ORD008","Laptop",75000,"Completed"] ]
# for index, order in enumerate(orders):
#     if (order[3] == "Completed"):
#         total_revenue += order[2]
# print(f"Total Revenue of Completed order is: {total_revenue}")

#4. Count Order Types Using loops and conditional statements, count how many orders fall into each category

orders = [ ["ORD001","Laptop",75000,"Completed"], ["ORD002","Mouse",500,"Completed"], ["ORD003","Laptop",75000,"Returned"], ["ORD004","Keyboard",1500,"Completed"], ["ORD005","Laptop",75000,"Completed"], ["ORD006","Monitor",20000,"Fraud"], ["ORD007","Mouse",500,"Completed"], ["ORD008","Laptop",75000,"Completed"] ]
category_list = list()
# Just get unique values for Category rather than hardcoding them.
for index, order in enumerate(orders):
   if (order[3] not in category_list):
        category_list.append(order[3])
completed_count = 0
returned_count = 0
fraud_count = 0
for i, order in enumerate(orders):
    if (order[3] == category_list[0]):
        completed_count += 1
    if (order[3] == category_list[1]):
        returned_count += 1  
    if (order[3] == category_list[2]):
        fraud_count += 1
# print(f"The frequency of - {category_list[0]} is {completed_count}") 
# print(f"The frequency of - {category_list[1]} is {returned_count}") 
# print(f"The frequency of - {category_list[2]} is {fraud_count}") 
        
# 5. Generate a List of Unique Products Create a new list containing unique product names present in the dataset. 
# You must implement this without using the set() function.
orders = [ ["ORD001","Laptop",75000,"Completed"], ["ORD002","Mouse",500,"Completed"], ["ORD003","Laptop",75000,"Returned"], ["ORD004","Keyboard",1500,"Completed"], ["ORD005","Laptop",75000,"Completed"], ["ORD006","Monitor",20000,"Fraud"], ["ORD007","Mouse",500,"Completed"], ["ORD008","Laptop",75000,"Completed"] ]
unique_product_list = list()
# Just get Unique Products
for index, order in enumerate(orders):
   if (order[1] not in unique_product_list):
        unique_product_list.append(order[1])
# print(f"Unique Products - {unique_product_list}") 


# 6. Product Sales Analysis For each unique product, determine: how many times it was ordered total revenue generated by that product 
# This requires nested loops.

# max_sold_product = 0
# max_sold_product_name = ''
# max_sold_product_count = 0
# max_sold_product_revenue = 0
# for i, unique_product in enumerate(unique_product_list):
#     count = 0
#     revenue = 0

#     # print(unique_product)
#     for j, order in enumerate(orders):
#         if(order[1] == unique_product and order[3] == "Completed"):
#             count += 1
#             revenue += order[2]
#         if ( max_sold_product_count < count):
#             max_sold_product_count = count
#             max_sold_product_name = order[1]
#             max_sold_product_revenue += order[2]
#     print(f"The Product '{unique_product}' was sold '{count}' times and the Revenue generated was - Rs. '{revenue}'")
    
# 7. Identify the Most Sold Product Based on the frequency of orders, determine which product appears the most in the dataset.
# print(f"The Product '{max_sold_product_name}' was sold Max times and that is: '{max_sold_product_count}' and it collected Rs. {max_sold_product_revenue}")

# Remove Fraud Orders Create a cleaned dataset by removing orders whose status is "Fraud". 
# Use list methods to store the cleaned data in a new list.
headers = ["Order ID" , "Product Name" , "Price" , "Status"]
orders = [ ["ORD001","Laptop",75000,"Completed"], ["ORD002","Mouse",500,"Completed"], ["ORD003","Laptop",75000,"Returned"], ["ORD004","Keyboard",1500,"Completed"], ["ORD005","Laptop",75000,"Completed"], ["ORD006","Monitor",20000,"Fraud"], ["ORD007","Mouse",500,"Completed"], ["ORD008","Laptop",75000,"Completed"] ]

cleaned_product_list = list()

for index, order in enumerate(orders):
    if (order[3] == "Fraud") :
        orders.pop(index)
        
cleaned_product_list = orders
print("-" * 55) # Separator line
print(f"{headers[0]:<15}{headers[1]:<15}{headers[2]:<15}{headers[3]:<15}")
print("-" * 55) # Separator line
for index, cleaned_order in enumerate(cleaned_product_list):
    print(f"{cleaned_order[0]:<15}{cleaned_order[1]:<15}{cleaned_order[2]:<15}{cleaned_order[3]:<15}")