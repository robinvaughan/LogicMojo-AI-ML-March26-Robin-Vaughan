                                    ###   Assignment 3     ###

# Question 3:- An analyst wants to compare the price of products listed on two e-commerce platforms.
# The following data is provided: products = ["Laptop","Phone","Tablet","Monitor","Headphones"] 
# amazon_prices = [75000, 45000, 30000, 20000, 5000] 
# flipkart_prices = [72000, 47000, 31000, 19500, 4800]
# Write a Python program that:
    # Combines the product names and their prices into a single data structure representing a table.
    # Compares the price of each product across both platforms.
    # Determines which platform offers the lower price.
    # Calculates the difference between the two prices.
    # Displays the product name, cheaper platform, and price difference.


products = ["Laptop","Phone","Tablet","Monitor","Headphones"] 
amazon_prices = [75000, 45000, 30000, 20000, 5000] 
flipkart_prices = [72000, 47000, 31000, 19500, 4800]


# Combines the product names and their prices into a single data structure representing a table.
# product_with_total_info = list(zip(products, amazon_prices, flipkart_prices))
# The above creates a LIST of Tuples that we DO NOT want, we want a list which contains lists.

product_with_total_info = [list(pair) for pair in zip(products, amazon_prices, flipkart_prices)]
# print(product_with_total_info)



# Compares the price of each product across both platforms.
counter_cheap_product_on_amazon     = 0
counter_cheap_product_on_flipkart   = 0
cheap_product_on_amazon             = list()
cheap_product_on_flipkart           = list()

for index, product in enumerate(product_with_total_info):
    product_name = product[0]
    amazon_price = product[1]
    flipkart_price = product[2]

    if (amazon_price < flipkart_price):
        print(f"The Product - '{product_name}' is cheaper on Amazon, buying from Amazon would save the amount -'{flipkart_price-amazon_price}'")
        counter_cheap_product_on_amazon = counter_cheap_product_on_amazon + 1
        cheap_product_on_amazon.append(product_name)
    elif (amazon_price > flipkart_price):
        print(f"The Product - '{product_name}' is cheaper on Flipkart, buying from Flipkart would save the amount -'{amazon_price-flipkart_price}'")
        counter_cheap_product_on_flipkart = counter_cheap_product_on_flipkart + 1
        cheap_product_on_flipkart.append(product_name)
    else:
        print ("Prices match :)")
print("\n")    
print(f"There are {counter_cheap_product_on_amazon} Products which are cheaper on Amazon and they are - {cheap_product_on_amazon}")
print(f"There are {counter_cheap_product_on_flipkart} Products which are cheaper on Amazon and they are - {cheap_product_on_flipkart}")