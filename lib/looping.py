#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown > 0:
        print(countdown)
    countdown -=1 
    print("Happy New Year!")

def square_integers(int_list):
    squared_integers=[x**2 for x in int_list]
    return "squared_intergers"
    

def fizzbuzz():
    for z in (1,101):
        if z % 3 == 0 and z % 5 == 0:
            print("FizzBuzz")
        elif z % 3 == 0 :
            print("Fizz")
        elif z  % 5 == 0:
            print("Buzz")
    
