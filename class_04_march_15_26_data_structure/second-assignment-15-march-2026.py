                                    ###   Assignment 2     ###

# Question 2:- A dataset exported from a database contains the following customer age values.

# ages = [25, 42, -1, 34, None, 52, 17, -5, 29, None, 46] 
# Some entries are invalid because they are either negative numbers or missing values (None).
# Write a Python program that:
    # Iterates through the dataset and removes all invalid age values.
    # Stores only valid ages in a new list.
    # Calculates the average age of valid customers.
    # Displays the list of customers whose age is greater than 30.
    # Prints how many invalid entries were removed during the cleaning process.

ages = [25, 42, -1, 34, None, 52, 17, -5, 29, None, 46] 

# Iterates through the dataset and removes all invalid age values.
for index, age in enumerate(ages):
    if (age is None or age < 0):
        ages.pop(index)
print(f"The Valid list for Ages is - {ages}")



# Stores only valid ages in a new list.
new_list_one = list()
for index, age in enumerate(ages):
    if (age is not None or age > 0):
        new_list_one.append(age)
print(f"Newly created Valid list of Ages is - {new_list_one}")



# Calculates the average age of valid customers.
total_age = 0
for index, valid_age in enumerate(new_list_one):
    total_age += valid_age
average_age = total_age/len(new_list_one)
print(f"Average of Valid Ages - {average_age}")



# Displays the list of customers whose age is greater than 30.
for index, valid_age in enumerate(new_list_one):
    # From the same list remove/pop all items that are less than 30 :) 
    # That way you get a list in which all items are more than 30 :)
    if (valid_age < 30) :
        new_list_one.pop(index)
print(f"Above 30 list of Valid Ages - {new_list_one}")



# Prints how many invalid entries were removed during the cleaning process.
# Just added the List again :)
ages = [25, 42, -1, 34, None, 52, 17, -5, 29, None, 46] 
entries_removed = 0
for age in ages:
    if (age is None or age < 0):
        entries_removed = entries_removed + 1
print(f"Number of invalid entries were removed during the cleaning process. - {entries_removed}")