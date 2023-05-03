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

# data structure
# 1. list []
# 2. tuple ()
# 3. dictionary {}
# 4. set {unique}

# list
## list is mutable - we can update values in it
shopping_item = ["banana", "eggs", "milk"]
print (shopping_item [0])
print (shopping_item [1:3])
print (len (shopping_item) )

shopping_item [0] = "pineapple"
print (shopping_item)

## list method - function that were created to use with only list
# add new item to list .append
shopping_item.append ("bread")
print (shopping_item)

# sort items -- default a-z (ascending order)
shopping_item.sort (reverse=True) # descending order
print (shopping_item)

# list with int or float

def mean (scores):
    return sum(scores) / len(scores)

scores = [90, 85, 79, 50, 93, 68, 77]
print (len(scores), sum (scores), min (scores), max(scores), mean (scores)) 
# base python default doesnt know function AVG() bruh -*-


# remove last item in list
shopping_item.pop()
print (shopping_item)

# remove selected item in list
shopping_item.remove("milk")
print (shopping_item)

# .insert()
shopping_item.insert(1, "milk")
print(shopping_item)

# list + list
items1 = ["egg", "milk"]
items2 = ["banana", "bread"]

print (items1 + items2)

# tuple () is immutable
tup_items = ('egg', 'bread', 'pepsi', 'egg', 'egg')
#tup_items[0] = 'coke' #error!

tup_items.count ('egg')


## username and password
s1 = ("id001", "123456")
s2 = ("id002", "654321")
user_pw = (s1, s2)
print (user_pw)

## tuple unpacking
username, password = s1 # pakard variable by unpack datapoint in tuple directly to username and pass

print(username, password)

## tuple unpacking 3 values
name, age, _ = ("Anawin", 42, 3.98) # use underscore "_" to not want that variable to be printed
print(name, age)

# set {unique}
courses = ["Python", "R", "SQL", "SQL", "Python", "Python", "R"]
set (courses) # similar to select distinct in SQL

# dictionary, {key:value} pairs, key is immutable 
course = {
    "name": "Data Science Bootcamp",
    "duration": "4 months",
    "students": 200,
    "replay": True,
    "skills": ["Google Sheets", "SQL", "R", "Python",
               "Stats", "ML", "Dashboard", "Data Transformation"]
}

# dueng ao value jark key
course ["name"] # cannot use course [0]
course ["skills"] [0:3]
course ["skills"] [-3: ]

course ["start_time"] = "9am" # create new key and value to dictionary

#delete key from dic
del course ["start_time"]

# update key in dic
course ["replay"] = False


# course method
list (course.keys()) #convert to list
list (course.values())
list (course.items())
course.get("replay") #even we type the key's name wrong, it is not error because it doesnt exist
#unlike course ["replays"] which return error message of code!

# recap
# list, dictionary = mutable
# tuple, string = immutable

# control flow
# if for while

# if condition, final exam 150 questions, pass >=120
def grade (score):
    if score >= 120:
        return ("passed")
    else:
        return ("failed")

result = grade (122)
print (result)

# multiple condition
def grade (score):
    if score >= 120:
        return ("Excellent")
    elif score >= 100:
        return ("Good")
    elif score >= 80:
        return ("Okay")
    else: 
        return ("need to work more")

grade (77)

## use and, or in condition
## course == data science, score >= 80 passed
## course == english, socre >= 70 passed
def grade (course, score):
    if course == "english" and score >= 70:
        return "passed"
    elif course == "data science" and score >= 80:
        return "passed"
    else:
        return "failed"

grade ("english", 69)

## for loop
# if score >= 80, passed
scores = [88, 90, 75]
new_scores = []


for score in scores:
    new_scores.append (score-2)

print (new_scores)

## defy function
def grading_all_stu (scores):
    new_scores = []
    for score in scores:
        new_scores.append (score + 3)
    return new_scores

grading_all_stu ([74, 88, 42, 98, 67])

## list comprehension
scores = [74, 88, 42, 98, 67]

for s in scores:
    print (s*2)

# shorter code - list comprehension
[s*2 for s in scores]

# another example
friends = ["jino", "yumi", "victor", "jay", "boss"]
for f in friends:
    print(f.upper())

[f.upper() for f in friends]

## while loop
# loop t run pai lueay2 jon kua ja mi condition phuea hai ork jark loop
# ex. chatbot with user until meet condition ("typing exit")
count = 0
while count < 5:
    print ("Hello!")
    count += 1

# input function
user_name = input ("What is your name? ")

user_name # value t hao input into tua box ja khao ma nai user_name variable lei

# chatbot for fruit order
def chatbot():
    fruits = []
    while True:
        fruit = input ("What fruit do you want to order? ")
        fruits.append(fruit)
        if fruit == "exit":
            return fruits

chatbot()

## HW01 - chatbot to order pizza
## HW02 - rock, paper, sciscor
## HW03 - OOP -- create new ATM class (fark ngern, thorn ngern, own ngern)

class ATM:
    def __init__ (self, name, bank, balance):
        self.name = name
        self.bank = bank
        self. balance = balance
    
    def deposit (self, amount):
        self.balance += amount


scb = ATM("bankkykun", "scb", 500)
print (scb.balance)

scb.deposit(100)
print (scb.balance)

age = int (input ("How old are you?"))

print (type (age))

# OOP - Object Oriented Programing
# OOP หรือชื่อเต็มๆก็คือ Object Oriented Programming อ่านแปลคร่าวๆก็คือการเขียนโปรแกรมเชิงวัตถุ ซึ่งเป็นแนวคิดในการพัฒนาซอฟแวร์ที่และเป็นที่ยอมรับ เ
#นื่องจากซอฟแวร์ที่ถูกพัฒนาและใช้กันอยู่นั้น นับวันมีแต่จะซับซ้อนมากยิ่งขึ้น ถ้าหากไม่จัดการกับโค้ดให้ดีพอก็อาจจะทำให้การพัฒนาล่าช้าหรือไม่สำเร็จได้  
#OOP จึงออกแบบมาให้โค้ดที่เราเขียนมีแบบแผนที่เหมาะสมพร้อมใช้ในการพัฒนาที่ซับซ้อนได้
#อย่างที่บอกไปด้านบนว่า OOP นั้นเเป็นการเขียนโปรแกรมเชิงวัตถุ เราก็ต้องลองเทียบกับวัตถุในชีวิตจริงของเราดูอย่างเช่น นก ในที่นี้เราจะให้นกเป็นวัตถุ 
# โดยสิ่งที่นกต้องมีก็คือ “คุณสมบัติ” เช่น สีเขียว, ปากยาว เป็นต้น และก็ต้องมี “พฤติกรรม” เช่น บิน, กินอาหาร เป็นต้น การเขียนโปรแกรมก็ต้องทำให้
#โค้ดของเรามีคุณสมบัติและพฤติกรรมเช่นเดียวกันกับนก แต่ว่าเพียงแค่นี้ก็ยังไม่นับว่าเป็น OOP เพราะว่า OOP ที่แท้จริงยังต้องมี 4 เสาหลักของ OOP 
# อยู่ด้วยได้แก่ Encapsulation Abstraction Inheritance Polymorphism อย่าเพิ่งงงกับศัพท์พวกนี้ เดี๋ยวเราไปดูกันว่าแต่ละตัวนั้นคืออะไรบ้าง

# teach python to know dog class
# __ dunder- double underscore
# class leo pass, jark nun jg luep pass ork and sai def
class Dog:
    def __init__ (self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

dog = Dog ()
print (dog)

dog1 = Dog ("charuru", 2, "Samoyed")
dog2 = Dog ("ditto", 3, "Puddle")
dog3 = Dog ("bigbagie", 1.5, "Golden Retriever")
# sue nrng mar ja thuek map khao pai name, name ka ja map pai t sue khrng object t hao sarng khuen ma, dog1,2,3 pai t self

print (dog1.name, dog1.age, dog1.breed)
print (dog2.name, dog2.age, dog2.breed)

class Employee:
    def __init__ (self, id, name, dept, pos):
        self.id = id
        self.name = name
        self.dept = dept
        self.pos = pos #position

    def hello (self): # function t sarng only in employee class, which is called "method"
        print (f"Hello! my name is {self.name}")

    def work_hours (self, hours):
        print (f"{self.name} works for {hours} hours.")
        
    def change_dept (self, new_dept):
        self.dept = new_dept
        print (f"{self.name} is now in {self.dept}.")

emp1 = Employee (1, "John", "Finance", "Financial Analyst")

print (emp1.name, emp1.pos)

emp1.hello()

emp1.work_hours(10)

emp1.dept

emp1.change_dept("Data Science")

# emp1.dept without () - this is "attribute" -- tua pae t u nai john
# emp1.change_dept() - this is method

## object in class
## object: attribute => name, id, dept, pos
## object: method => hello(), change_dept()

