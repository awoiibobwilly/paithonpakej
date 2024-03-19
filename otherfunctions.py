def add1 ():
    num1, num2, num3 = 10, 20, 50
    sum = num1 + num2 + num3
    print(sum)
add1()

def add2 ():
    num4, num5 = 60, 70
    sum = num4 + num5
    print(sum)
add2()

#CREATING A DYNAMIC FUNCTION
def add3 (num6, num7, num8):
    sum = num6 + num7 + num8
    print(sum)
add3(100,150,200)
add3(300,450,500)
add3(600,750,800)


def mult1 (num1, num2):
    mult = num1 * num2
    print(mult)
mult1()


#MULTIDATA
def multidata (num1, num2, name, flt):
    print(num1)
    print(num2)
    print(name)
    print(flt)
multidata(10, 20, 'bob', 10.2)
    
def multidata (name, age, height, weight, location):
    print(name)
    print(age)
    print(height)
    print(weight)
    print(location)
multidata("Awoii Bob Willy", "41 Years", "5.6 Ft", "59 Kg", "Ntinda")
def hack(name, year_of_birth, district):
    """print(name)
    print(year_of_birth) 
    print(district)"""
    currentYear = 2024
    age = currentYear - year_of_birth
    print(name, "is", age)
hack("bob", 1982, "Agago")