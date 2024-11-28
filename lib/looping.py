#!/usr/bin/env python3


def happy_new_year():
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1  
    print("Happy New Year!")  


def square_integers(int_list):
    
    squared_integers = [x**2 for x in int_list]
    return squared_integers  
    

def fizzbuzz():
    for i in range(1, 101):  
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")  
        elif i % 3 == 0:
            print("Fizz")  
        elif i % 5 == 0:
            print("Buzz")  
        else:
            print(i)  
