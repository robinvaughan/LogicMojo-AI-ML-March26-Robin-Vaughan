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