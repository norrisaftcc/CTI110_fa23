# CTI 110
# P4T2 - Time cards
# norris
# 10/5/23

# Get the user's work info for the week
# Find the pay
"""
# Take 1: Use a list
hours = [8, 8, 8, 7, 9]
print("You worked:")
total_hours = sum(hours)
print(total_hours, "hours")
print("Longest shift was", max(hours), "hours")
print("Shortest shift was", min(hours), "hours")
# find the average
average = total_hours / len(hours)
print("For an average of", average, "hours per shift.")
"""

# Take 2 : by hand
print("Timecard program")
# Set up variables
DAYS_OF_WEEK = 5 # constant
todays_hours = 0
total_hours = 0
# Ask for time worked for each day
# and take a running total
for day in range(DAYS_OF_WEEK):
    print("Hours worked for day", day+1, end=":") # we'll print 1-5, not 0-4
    todays_hours = float(input())
    #total_hours = total_hours + todays_hours # or, 
    total_hours += todays_hours # shortcut += operator
# Print the total and average hours
print("Total hours this week:" , total_hours)
average_hours = total_hours / DAYS_OF_WEEK
print("Average shift time:", average_hours, "hours")
