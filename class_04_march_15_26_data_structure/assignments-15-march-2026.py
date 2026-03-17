
                                    ###   Assignment 1     ###


# Question 1:- A digital payment platform recorded the following transaction amounts made by a 
# customer during a single day.

# transactions = [1200, 3000, 250, 7800, 540, 3000, 9100, 250, 1500, 7800]

# Write a Python program that performs the following analysis:
    # Identify and display all transaction values that appear more than once.
    # Detect transactions greater than ₹5000 as these may require fraud monitoring.
    # Calculate the total spending for the day.
    # Create a new list containing only unique transaction values.
    # Sort the unique transaction list in descending order to view the largest transactions first.
    
transactions = [1200, 3000, 250, 7800, 540, 3000, 9100, 250, 1500, 7800]

# Identify and display all transaction values that appear more than once.
test_list_one = list()
for transaction in transactions:
    frequency = transactions.count(transaction)
    if (frequency > 1):
        if (transaction in test_list_one):
            print(f"The Frequency of transaction -'{transaction}' is - '{frequency}'")
    test_list_one.append(transaction)
