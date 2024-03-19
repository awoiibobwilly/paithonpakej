#A named block of codes is called a function
#A named group of statements is called a function
#Languages are built on the notion of functions
#In a language once you master the art of functions, you have mastered that language
#Functions are the building of programming languages
#For example,

def my_function(): #def is a short name for defining 
    num1, num2 = 20, 40
    print(num1 + num2)

#A function is a group of related statements that are performing specific tasks

my_function()

#TYPES OF FUNCTIONS
#There are two types of functions
#A Static functions are functions that are created without thing in in
#Dynamic functions are functions that are created created with things in it.

boblist = [10,20,30,40,50]

def loops1():
    for i in boblist:
        print(i)

def loops2():
    for item in boblist:
        print(item)


def loops3():
    for i in range(10):
        print(i)

item = 1

def loops4():
    for i in range(10):
        print(item)
        item = item + 1

def loops5():
    for item in range(1,10): 
        print(item)

def loops6():    
    for it in range(1,20):
        if item % 2 == 0:
            print(item)

def loops7():
    for it in range(1,20):
        if item % 2 != 0:
            print(item)

        
digits = [23,67,50,89]
def loops8():
    for i in digits:
        print(i)
    else:
        print("no items left") 
    
lake_victoria = {"Type:": "Fresh Water Body", "Description:": "Largest in East Africa", "Type of Found:": "Tilapia and Nile Perch", "Stretch:": "Uganda, Kenya, Tanzania"}

def loops9():
    for keys, values in lake_victoria.items():
        print(keys, values)

loops9()

loops8()

#Functions are groups of codes with names
#Whwn creating functions we use def (meaning definition)
#Static functions (what is inside the parentheses, all variables have hard coded values, functions need to be called)

def condition ():
    number = 10 #From this (80) line to line 83, this is a function definition
    if number > 0:
        print('number is positive')
    print('the if statement is easy') #This is a function definition
    
#A function is not created, it is defined, so is the word def
#Anything indented within a function is a function definition
        
#condition() 

#The below code is when we remove/extracted this pice of code from the above function

number = 10
if number > 0:
    print('number is positive')

condition()

"""
function condition(){
    
}

This is how the JavaScript is written, while in python we use ':' and indentation
"""

#The calling out of a function is called invoking a function

def mycondition():
    number = -10
    if number > 0:
        print('number is positive')
    else:
        print('number is negative')
    print('this satement is not related to if or else, but in the same function')
    
mycondition()

#A function will be a dead code if it is not called