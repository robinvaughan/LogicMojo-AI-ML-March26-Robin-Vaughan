                                    ###   Assignment 4     ###

# Question 4:- A web platform records the hours when users log into the system.

# login_hours = [1, 3, 5, 7, 2, 6, 8, 4, 9, 10] 
# Write a Python program that:
    # Separates login hours into even-hour logins and odd-hour logins.
    # Identifies login hours that fall into peak activity time (hours greater than 5).
    # Sorts the login hours in ascending order.
    # Calculates how many logins occurred during peak hours.

evenHourLogins = list()
OddHourLogins = []

login_hours = [1, 3, 5, 7, 2, 6, 8, 4, 9, 10]

for index, login_hour in enumerate(login_hours):
    if(login_hour%2 == 0):
       evenHourLogins.append(login_hour)
    else:
        OddHourLogins.append(login_hour)

print (f"Even-hour logins - {evenHourLogins}")
print (f"Odd-hour logins - {OddHourLogins}")



# Identifies login hours that fall into peak activity time (hours greater than 5) &
# Calculates how many logins occurred during peak hours.

login_hours = [1, 3, 5, 7, 2, 6, 8, 4, 9, 10]
peakActivityTime = list()
counter = 0
for index, login_hour in enumerate(login_hours):
    if(login_hour > 5):
        peakActivityTime.append(login_hour)
        counter += 1
print(f"This are {len(peakActivityTime)} that fall in Peak activity-{peakActivityTime}")
print(f"The number of logins occurred during peak hours is - {counter}")



# Sorts the login hours in ascending order.
login_hours = [1, 3, 5, 7, 2, 6, 8, 4, 9, 10]
login_hours.sort()
print(f"Login hours in ascending order - {login_hours}")
