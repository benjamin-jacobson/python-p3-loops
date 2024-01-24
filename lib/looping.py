#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    x = 10
    while (x > 0):
        x -= 1
        print(x)
        if x == 1:
            print("Happy New Year!")
            break

def square_integers(int_list):
    # code goes here!
    x = [i ** 2 for i in int_list]
    print(x)
    return x

def fizzbuzz():
    # code goes here!
    for i in range(101):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(i)