# -*- coding: utf-8 -*-

# -- Sheet --

print("hello world!")



# in python the code always run only in the most bottom line, if you want to run every line and show in console
# you must use function print()
1+3
4+5

print (1+3)
print(4+5)

7//2 # floor division, br ao lek thotsaniyom, unlike 7/2 = 3.5

pow(5, 2)

abs(-666)

# modulo, to check va mun harn long tua br (br mi sed suan), if br long tua mun ja return 1, if long tua return 0
5 % 2

# 5 building blocks of programing language
# 1. Variables
# 2. Datatypes
# 3. Data structures
# 4. function
# 5. controlflow

# assign variables and datatypes
my_name = "bank" # string
my_age = 25 # integer
gpa = 3.44  # float or real number
movie_lover = True #boulean


#count variable
age = 35
age += 5 # equal to age + 5 (shorter syntax)

# check data types
print ( type(my_age) )
print ( type (gpa) )

# convert type with function str(), int(), bool(), float()
x = 100
x = str (x)
print (x, type (x) )

y = True #T=1, F=0
y = int (y)
print (y, type (y))

# concatenate text with + operator
text_1 = "Hello"
text_2 = ' "I am loving it" '
print (text_1 + text_2)
print (text_1 * 4)

# type hint, its just a hint but not enforced -- still rely on the variables ex age: int = "34" - <class str>
age: int = 34
name: str = "Bank"
gpa: float = 3.14
movie_hater: bool = False


# function
print ("Hello", 25, "people")
print (pow (5,2), abs(-5))

## greeting function -- create our own function def()
def greeting (firstname = "toy", id = "15", location = "London"):
    print ("Hello! " + firstname + ". Your ID is " + id + ". Your location is " + location)

greeting (id = "13", firstname = "Bank", location = "London") # mun ja run thup default argument lei, positional mappping

def add_two_nums (x: int, y: int) -> int:  # -> result t ork ma must be int!
    print ("Hello World!")
    return (x + y)

result = add_two_nums(4,5) 
print (result) 

# print dif from return is "return man karn song khar y kup ma phuea t hao samard ao khar nun pai pa kard khar nai to pae mai"
# e y ka yar t u after return in function, commmand nun ja jop and yout u nun ex. if we khien print ("done") after return
# ja run br ork

# work with string 
text = "Hello world!"
long_text = """This is a very long text
This is a new line
just use triple quote :)"""

print(long_text)

## string template : fstrings
his_name = "John Wick"
his_lo = "London"

his_text = f"Hi! my name is {his_name} and I live in {his_lo}"

print (his_text)

##  before they use .format instead of fstring
"Hi my name is {}, and I live in {}". format (his_name, his_lo)

## subseting or slicing the text from the sentence
text02 = "a duck walks into a bar"
print (text02)

len(text02)

# slicing index starts from 0
print ( text02 [0], text02 [-1], text02 [22])
print ( text02 [2:6]) # python index lerm t 2 up into 5 but not included, sa nun hao trng sai index to 6 phuea khum va duck
print ( text02 [-3: ])

## string is immmutable (bor sa mard pien paeng dai)
code = "Python" # if we want to change to -> Cython
#code [0] = "C"
#print (code) # ERROR

code = "C" + code [1: ]
print (code)

## function vs. method
## string methods "." is function t sarng khuen ma sumlup object nun2, only works with string!
text02 = "a duck walks into a bar"
text02 = text02.upper()
text02_rep = text02.replace("DUCK", "LION")
text02_split = text02.split(" ")
print (text02)
print (text02_rep)
print (text02_split, type (text02_split)) # class list

"-".join(text02_split)



