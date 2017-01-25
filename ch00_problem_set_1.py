#SECTION 1 - MATH OPERATORS AND VARIABLES (20PTS TOTAL)
import math
#PROBLEM 1 (From Math Class to Code - 2pts)

# Print the answer to the math question:
# 3(60x^2 + 3x/9) + 2x - 4/3(x) - sqrt(x)
# where x = 12.83
x = 12.83
your_answer = 3*(60*x*x+(3*x/9))+2*x-((4/3)*x)-math.sqrt(x)
print(your_answer)

#PROBLEM 2 (Set your alarm - 3pts)

#You look at the clock and see that it is currently 1:00PM.
# You set an alarm to go off 728 hours later.
# At what time will the alarm go off? Write a program that prints the answer.
# Hint: for the best solution, you will need the modulo operator.
sat=1
vreme=1
alarm=728
vreme=vreme+alarm
dzvoni=0
dzvoni=vreme-((vreme//24)*24)
if (dzvoni+sat)>0 and (dzvoni+sat)<=12:
    print(dzvoni+sat,"PM")
elif (dzvoni+sat)>12:
    print((dzvoni+sat)-12,"AM")
#PROBLEM 3 (Wholesale Books - 3pts)
#The cover price of a book is $27.95, but bookstores get a 50 percent discount.
#Shipping costs $4 for the first copy and 75 cents for each additional copy.
# Calculate the total wholesale costs for 68 copies to the nearest penny.

#i know i know, variables. was too lazy to do that
#im also not not sure of the numerical representation of a penny (0.1) (0.01) ?
answer=((27.95*0.5)-4+67*((27.95*0.5)-0.75))
print(answer)

#PROBLEM 4 (Dining Room Chairs - 3pts)
# You purchase eight chairs for your dining room.
# You pay for the chairs plus sales tax at 9.5%
# Make a program that prints the amount to the nearest penny using the variables below
# Use the round(float, digits) function to get to nearest penny
chair_price = 189.99
tax_percent = 0.095
units = 8
amount=chair_price*tax_percent*units
print(round(amount,2))

#PROBLEM 5 (Area of Circle - 3pts)
# Write code that can compute the area of circle.
# Create variables for radius and pi (3.14159)
# The formula, in case you do not know, is radius times radius times pi.
# Print the outcome of your program as follows:
# “The surface area of a circle with radius ... is ...”
radius=3
pi=math.pi
rezultat=radius*radius*pi
print("The surface area of a circle with radius",radius,"is",rezultat)
#PROBLEM 6 (Coin counter - 4pts)
# Write code that classifies a given amount of money (which you store in a variable named count),
# as greater monetary units. Your code lists the monetary equivalent in dollars, quarters,
# dimes, nickels, and pennies.
# Your program should report the maximum number of dollars that fit in the amount,
# then the maximum number of quarters that fit in the remainder after you subtract the dollars,
# then the maximum number of dimes that fit in the remainder after you subtract the dollars and quarters,
# and so on for nickels and pennies.
# The result is that you express the amount as the minimum number of coins needed.

#We shall assume 1 dollar=100 pennies, 4 quartets, 10 dimes and 20 nickels
count=7.28
dolari=count//1
quarters=(count%dolari)//0.25
dimes=((count%dolari)-(quarters*0.25))//0.1
current_count=(count-dolari-(quarters*0.25)-(dimes*0.1))
nickels=(current_count//0.05)
pennies=(current_count%0.05)//0.01

print(pennies+dimes+nickels+quarters)

#PROBLEM 7 (Variable Swap - 2pts)
# Can you think of a way to swap the values of two variables that does not
# need a third variable as a temporary storage?
# In the code below, try to implement the swapping of the values of 'a' and 'b' without using a third variable.
# To help you out, the first step to do this is already given.
# You just need to add two more lines of code.

a = 17
b = 23
print( "a =", a, "and b =", b)
a += b
b=a-b
a=a-b
# this is the first line to help you out
# add two more lines of code here to cause swapping of a and b
print( "a =", a, "and b =", b)