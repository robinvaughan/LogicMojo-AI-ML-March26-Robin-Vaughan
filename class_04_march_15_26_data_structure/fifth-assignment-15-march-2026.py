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


headers = ["Order ID" , "Product Name" , "Price" , "Status"]
orders = [ ["ORD001","Laptop",75000,"Completed"], ["ORD002","Mouse",500,"Completed"], ["ORD003","Laptop",75000,"Returned"], ["ORD004","Keyboard",1500,"Completed"], ["ORD005","Laptop",75000,"Completed"], ["ORD006","Monitor",20000,"Fraud"], ["ORD007","Mouse",500,"Completed"], ["ORD008","Laptop",75000,"Completed"] ]
print("~" * 60) # Separator line
print(f"{headers[0]:<15}{headers[1]:<15}{headers[2]:<15}{headers[3]:<15}")
print("~" * 60) # Separator line
for index, order in enumerate(orders):
    print(f"{order[0]:<15}{order[1]:<15}{order[2]:<15}{order[3]:<15}")
    print("-" * 60) # Separator line
