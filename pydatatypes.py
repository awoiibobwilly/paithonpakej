#DATA TYPES IN PYTHON (Different kinds of data we store in the memory)
# Data types helps us to efficiently use memory so that we are not wasteful    
# Data types are different kinds of data that we store in memory
# DATA TYPES
# 1- Numeric types
# 2- String types
# 3- Sequence types
# 4- Mapping types
# 5- Boolean types
# 6- Set types

# NUMERIC types
# we write integer (int) and float (float) and complex (complex)
# EXAMPLE  

num1 = 10
print (num1, "is of a type", type (num1))

num2 = 100
print (num2, "is of a type", type (num2))

num3 =23.4
print (num3, "is of a type", type (num3))

num4 = 3+6j
print (num4, "is of a type", type (num4))

#This is 11/04/2024 Class 

country= ["uganda", "kenya", "tanzania", ["egyptia", "somial", ["sudan", ["togo", ["benin",]]]]]
print(country [-1][-1][-1][-1])

fruits= ("apple","mango","orange", ["pawpaw","pear"])
print(fruits[0])
print(fruits[-1][-1])
print(fruits[3][1])
country.append ("Ghana")
print(country)

#tuples are immutable datadtypes, meaning thatyou can't change it
#tuples can be created

#mapping types

person={"name":"Awoii Bob Willy", "age":29, "email":"awoiibob@gmail.com", "country":"Uganda", "height":5}
print(person["name"])
print(person.values())

#set types (an unordered collection of unique values)
#A set is a collection of unique values or items

student_id={111,112,113,114,115,116,117,117}
print(student_id)
print(student_id)

district = ['Kampala', 'Kasese', 'Kamengo', 'Kabale',['Kotido', 'Kaabong',['Kumi',['Kisoro']]]]

print(district[0][1][2][4])