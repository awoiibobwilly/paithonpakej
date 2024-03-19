""" for unm in range (1,10):
    if unm > 10:
        print("numbers are out of range")
else:
    print("numbers were in range")

myrange = int(input("please enter your range"))

for unm in range (1, myrange):
    if unm > 10:
        print("numbers are out of range")
else:
    print("numbers were in range")

mylist = [1, 2, 3, 4, 5, 6, 7]
for i in mylist:
    print(i)
else:
    print("no itmes left")

    """


#WHILE LOOPS
    
begin = 1
end = 5


while begin <= end:
    print(begin)
    begin += 1

counter = 0
while counter < 5:
    print("these are the numbers in the range")
    counter += 1
else:
    print("outer of range")