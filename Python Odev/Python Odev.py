'''
Exercise 1
Write a shutting down program:

First, def a function, shut_down, that takes one argument s. Then, if the shut_down function receives an s equal to "yes",
it should return "Shutting down" Alternatively, elif s is equal to "no", then the function should return "Shutdown aborted".
Finally, if shut_down gets anything other than those inputs, the function should return "Sorry".
'''

def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "sorry"

print(shut_down("asdasd"))

"""
Exercise 2
Import the math module in whatever way you prefer. Call its sqrt function on the number 13689 and print that value to the console.
"""

import math
def excercise_2(ex2):
    return math.sqrt(ex2)

print(excercise_2(13689))

"""
Exercise 3
First, def a function called distance_from_zero, with one argument (choose any argument name you like). 
If the type of the argument is either int or float, 
the function should return the absolute value of the function input. Otherwise, the function should return "Nope". 
Check if it works calling the function with -5.6 and "what?".
"""

def distance_from_zero(ilike):
    if type(ilike) == float or type(ilike) == int:
        return abs(ilike)
    else:
        return "Nope"

print(distance_from_zero("fsdfd"))

'''
Exercise 4
Rewrite your pay computation program (previus chapter) with time-and-a-half for overtime 
and create a function called computepay which takes two parameters (hours and rate).
'''

def pay_computation():
    hours = int(input("Enter Hours: "))
    pay = int(input("Enter Pay: "))
    if (hours <= 40):
        return (hours * pay)
    else:
        return (((hours - 40) * (pay * 1.5)) + (pay*40))

# print(pay_computation())

'''
Exercise 5
Let's use functions to calculate your trip's costs:

Define a function called hotel_cost with one argument nights as input. The hotel costs $140 per night. 
So, the function hotel_cost should return 140 * nights.
Define a function called plane_ride_cost that takes a string, city, as input. 
The function should return a different price depending on the location, similar to the code example above. 
Below are the valid destinations and their corresponding round-trip prices.
"Charlotte": 183
"Tampa": 220
"Pittsburgh": 222
"Los Angeles": 475
-Below your existing code, define a function called rental_car_cost with an argument called days. 
Calculate the cost of renting the car: Every day you rent the car costs $40.(cost=40*days) 
if you rent the car for 7 or more days, you get $50 off your total(cost-=50). 
Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total. 
You cannot get both of the above discounts. Return that cost. -Then, define a function called trip_cost that takes two arguments, city and days. 
Like the example above, have your function return the sum of calling the rental_car_cost(days), hotel_cost(days), and plane_ride_cost(city) functions.
Modify your trip_cost function definion. Add a third argument, spending_money. 
Modify what the trip_cost function does. Add the variable `spending_money to the sum that it returns.
'''

def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    cities = {"Charlotte": 183,
              "Tampa": 220,
              "Pittsburgh": 222,
              "Los Angeles": 475}
    return cities[city]

def rental_car_cost(days):
    if days < 3:
        return days * 40
    if days < 7:
        return days * 40 - 20
    else:
        return days * 40 - 50

def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

print(trip_cost("Tampa", 7, 300))

'''
Exercise 6
Follow the stpes:

First, def a function called cube that takes an argument called number.
Make that function return the cube of that number (i.e. that number multiplied by itself and multiplied by itself once again).
Define a second function called by_three that takes an argument called number. 
if that number is divisible by 3,by_threeshould call cube(number) and return its result. Otherwise, by_three should return False. -Check if it works.
'''

def cube(number):
    return number * number * number

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

print(by_three(3))

#############----------ODEV 2---------#################

'''
Exercise 1
Follow the steps:

Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as arguments. 
Make sure to set these appropriately in the body of the __init__()method.
Create a variable named number_of_sides and set it equal to 3.
Create a method named check_angles. The sum of a triangle's three angles is 
It should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.
Create a variable named my_triangle and set it equal to a new instance of your Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
Print out my_triangle.number_of_sides and print out my_triangle.check_angles().
'''

class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2 #i wasted 30 min of my life because i put comas here :(
        self.angle3 = angle3

    number_of_sides = 3

    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False

my_triangle=Triangle(90,30,60)

print(my_triangle.number_of_sides)
print(my_triangle.check_angles())

'''
Exercise 2
Define a class called Songs, it will show the lyrics of a song. 
Its __init__() method should have two arguments:selfanf lyrics.lyricsis a list. 
Inside your class create a method called sing_me_a_songthat prints each element of lyricson his own line. Define a varible:

happy_bday = Song(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])
Call the sing_me_songmehod on this variable.
'''

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)

happy_birthday = Song(["May god bless you, ",
                       "Have a sunshine on you,",
                       "Happy Birthday to you !"])

happy_birthday.sing_me_a_song()

# I can't get rid of "None" going as the fourth printed item. I need help on explanation on it.

'''
Exercise 3
Define a class called Lunch.Its __init__() method should have two arguments:selfanf menu.Where menu is a string. 

Add a method called menu_price.It will involve a ifstatement:

if "menu 1" print "Your choice:", menu, "Price 12.00", if "menu 2" print "Your choice:", menu, "Price 13.40", else print "Error in menu".
To check if it works define: Paul=Lunch("menu 1") and call Paul.menu_price().
'''
class Lunch:
    def __init__(self, menu):
        self.menu = str(menu)

    def menu_price(self):
        if self.menu == "menu 1":
            print("Your choice: " + self.menu + ", Price: 12.00")
        elif self.menu == "menu 2":
            print("Your choice: " + self.menu + ", Price: 13.40")
        else:
            print("Error in menu")

Paul = Lunch("menu 1")
Jake = Lunch("menu 2")
Allen = Lunch("jak")

Paul.menu_price()
Jake.menu_price()
Allen.menu_price()

'''
Exercise 4
Define a Point3D class that inherits from object Inside the Point3D class, define an __init__() function that accepts self, x, y, and z, 
and assigns these numbers to the member variables self.x,self.y,self.z. Define a __repr__() method that returns "(%d, %d, %d)" % (self.x, self.y, self.z). 
This tells Python to represent this object in the following format: (x, y, z). Outside the class definition, 
create a variable named my_point containing a new instance of Point3D with x=1, y=2, and z=3. Finally, print my_point.
'''

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(x=1, y=2, z=3)

print(my_point)