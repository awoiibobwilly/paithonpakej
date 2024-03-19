boblist = [10,20,30,40,50]

for i in boblist:

    print(i)

for item in boblist:

    print(item)

#A loop is a mechanism in programming through which we tell the computer to do something until a certain condition is met or fulfilled.
    
#In the above example (code) we are carrying out iterations until a certain condition is met
    
    #Below is an iteration of values in a list of number

for i in range(10):
    print(i)

item = 1

for i in range(10):
    print(item)
    item = item + 1

for item in range(1,10): # 1 being the start index and 10 being the end
    print(item)

#Range is a keyword 
    
for it in range(1,20):
    if i % 2 == 0:
        print(i)

for it in range(1,20):
    if i % 2 != 0:
        print(i)

#A block of code is a collection of related statements
#Cloumn informs the indentation level of the code
        
#The above example, is syntax of four loop
        
#wildloops are
        
digits = [23,67,50,89]
for i in digits:
    print(i)
else:
    print("no items left") #Thus meaning, once done with the the previous command, execute this command

#The else statement works where there is a false statement
    
lake_victoria = {"Type:": "Fresh Water Body", "Description:": "Largest in East Africa", "Type of Found:": "Tilapia and Nile Perch", "Stretch:": "Uganda, Kenya, Tanzania"}
for keys, values in lake_victoria.items():
    print(keys, values)

