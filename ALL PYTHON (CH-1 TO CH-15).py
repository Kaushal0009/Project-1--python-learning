                                                                                                                        # chap -1 - Complete Course Python

# How to Use comments - we use "#" for comments
# How to Use escape series - Use of      \\, \n, \t,   in programs 
# How to Use Python as Calculater - print (2+3), print(2**3), print(5%2)

print("This is \\\\ double backslash")
print("These are  //\\//\\//\\//\\ mountains")
print("He is \tAwsome")
print('line_1 \nline_2')

# # Print("2+3")
# print(2**3)
# print(5%2)
# print(6/2)


# VARIABLES in Python:- Python uses DYNAMIC veriables. You should not need to define his data type and it 
# can change its value even throughout the program too. An Example is given bellow-

# Name_One = "Kaushal"            # Here Name_One is a veriable and "kaushal" is a value assign to it
# print (Name_One)                
# Name_One = "Soni"               # Here again we assign a diffrent value to same variable in same program.
# print (Name_One)

Name1 = "Hello"
Name2 =  123
print(Name1, Name2)



                                                                                                                                        # Chap -2 Summary
# What is string   -  "KAUSHAL" 'SONI'
# what is string Indexing - TO FIND THE LENGTH OF THE STRING
# What is String slicing 
# How to take User Input
# How to take 2 User Input
# Len - Function - TO FIND THE LENGTH OF THE STRING
# Methods - lower, upper, title 
# Methods - find, replace, Center 
# STRINGS ARE IMMUTABLE - MEANS YOU CAN NOT CHANGE THE VALUE OF THE STRING
'''
                           # EXAMPLE -1 
name = "kaushal"           # Dynamic veriable - No need to define data type
print(name[0])             # position start from 0 
print(name[-1])            # position start from -1 in reversal

                           # STRING SLICING  -  [ :  :  ]
name = "kaushal"
print(name[0])      
print(name[1])
print(name[0:4])
print(name[0:5:2])    

                                                             # USER INPUT - INPUT() FUNCTION 
name = input("Enter your Name - ")
print(name)

age = input("Enter your age - ")
print(age)

                                                             # 2 Inputs together - .split() 
Name, age = input('Enter your Name & Age ').split(',')
print(name, age)

                                                            # LEN Function - TO FIND THE LENTH OF THE STRING
name = "kaushal"
print(len(name))

                                                             #METHODS - LOWER, UPPER, TITLE 
name = "KaUsHaL"
print(name.lower())         # All character in Lower case
print(name.upper())         # All in Upper case
print(name.title())         # First in Upper and rest in lowercase

                                                            # Methods - find, replace, Center 

'''
                                                                                                            # tutorial 18- input function , Enter name 

# name = input("write your name ")
# print (" hello " + name )
# age = input("Enter your age ")
# print ("Your age is " + age)

# tutorial 19 - Int() function, Add two numbers

# num1, num2 = input ("Enter two numbers ").split()
# total = int(num1) + int(num2)
# print (" Total of two number is " + str(total))

# tutorial 21- Use of split() function

# name, last = Input (" Enter your First and Last ").split()
# Fullname = str(name) + str(last)
# print("your full_name is "+ Fullname)

# tutorial 22, String Formating {} , python 3 and python 3.6

# name, last = input(" write your name and last ").split()
# print(" Hello {} your last name is {}" .format(name, last))  # python 3 formating
# print(f" Hello {name} your last name is {last}")             # python 3.6 formating

# tutorial 23 - exercise - avarage of 3 numbers

# num1, num2, num3 = input(" Enter 1st, 2nd and 3rd number ").split()
# avarage = (int(num1)+ int(num2)+ int(num3))/3
# print(avarage)

# tutotial 25,26,27 - string indexing [], slicing[ : ], step slicing [ : : ] , use to index the string

# name = input (" Enter your name ") 
# # # name = "kaushalsoni"
# # print(name[2])
# # print(name[ : ])
# # print(name[0 : 5])
# # print(name[-1: : -1])
# print(f"Reverse of Your name is {name[-1: : -1]}") # python 3.6 string formating
# print(" Reverse of your name is {}" .format(name[-1::-1]))   # python 3 string formating


# tutorial 28 and 29 - exercise and solution


                                                                                    # methods- len() function, upper() method, lower, title,  count

# name = "kaushal soni"
# name = input(" what is your name ")

# print(len(name))     # to count total alphabets, inclued spaces

# print(name.title())  #title() method

# print(name.lower())  #lower() method

# print(name.count("k"))  #count() method use to check the count of same charactor  

# Tutorial 31,32- expercise

# name, ch = input ("Write your Full Name and the charactor you want to count ").split()

# print(f" lenth of your name is {len(name)}")
# print(f" The count of your character in the name is {name.strip().lower().count(ch.strip().lower())}")




# tutorial 33- strip method (lstrip, rstrip, strip) - to remove extra spaces 

# name = "     kaushal      "
# dots = ".................."
# print(name.strip() + dots)            # to remove all spaces from variable's value 
# print(name.lstrip() + dots)           # to remove Left spaces from variable's value
# print(name.rstrip() + dots)           # to remove ringht spaces

# Tutorial 34- replace method 

# line = " he is a good programmer and he "
# print(line)     #simple
# print(line.replace("he" ,"I"))    # to change all "he" with "I"
# print(line.replace("he", "I",1))  # to change specific "he" with "I" , 1 = 1st "he"

# find method - to get position of any string

# line = print( " hello everyone, I am a programmer and you?")
# ch = input(" enter the string from line, to find his position ")
# value = line.find(ch)
# print(f"The position of the string is {value}")     # this will give the position number of the string you enter

# TUTORIAL - 35 - CH-2 - CENTER METHOD (lenth of string, "symbol") - USED TO ADD "*" OR OTHER THING ON BOTH SIDES

# name = input(" Enter your name ")
# star = int(input("Enter the value of stars "))
# print(name.center(len(name) + star,"*"))              


# TUTORIAL - 36 - IMMUTABLE STRINGS
# IMMUTABEL MEANS WE CAN NOT MAKE ANY CHANGE IN THE ORIGINAL STRING

#TUTORIAL -37 - USE OF +=,-=, AND ALL

#TUTORIAL - 38  SUMMARY OF CH-2 





                                                                                                                       # CHAP-3 SUMMARY AND SOLUTIONS

# IF STATEMENT
# IF ELSE STATEMENT
# AND , OR - OPERATERS
# "IN" KEYWORD in IF STATEMENT





#TUTORIAL - 39 - USE OF "IF STATEMENT"

# name, age = input(" Hello, Please enter your Name and Age ").split()
# age = int(age)     # Because age is default data type is string      
# if age>=14:        # Check Condition
#     print("Congratulations, you are In Dear" + name)
    

#TUTORIAL - 40 - USE OF "PASS" STATEMENT

#TUTORIAL -41 - "ELSE" STATEMENT

# name, age = input(" Hello, Please enter your name and age ").split()
# age = int(age)
# if age>=14:
#     print("Congratulations, you are in Dear " + name)
# else:
#     print("sorry, under age")


# name, age = input("Enter your Name and age ").split()
# age = int(age)
# if age>=14:
#     print("Congratulations You are In Dear " +name.title())
# else:
#     print ("Sorry, You are Under age Dear " +name.title())



#TUTORIAL - 42- EXERCISE 

# name = input("Hye Dear, Please Enter Your Name ")
# jackpot = len(name)*2
# guess = input("Guess your Jackpot Number ")
# guess = int(guess)
# if guess == jackpot:
#     print("Congratulations, You win " +name.title())
# else :
#     if guess>jackpot:
#         print("Sorry, To High")
#     else :
#         print("Sorry, To Low")


# name = input("Enter your Name ")
# Jackpot = len(name)*2
# guess = input(" Enter your Jackpot Number ")
# guess = int(guess)
# if guess==Jackpot:
#     print("Congratulations, You won")
# else :
#     if guess>Jackpot:
#         print("Too High")
#     else:
#         print("Too Low")


#TUTORIAL 44 - AND, OR OPERATORS

# name, age = input("Enter your Name and age ").split()
# age = int(age)
# if name=="kaushal" and age==27:
#     print("Hello kaushal, System is ready to use")

# else:
#     print("Sorry, you are not Allowed to you system")


#TUTORIAL 45,46 - expercise AND SOLUTION

# name, age = input(" Enter your name and age ").split()
# age= int(age)
# if (name[0]=="a" or name[0]=="A") and age>=10:
#     print("Watch 'COCO' Movie")


#TUTORIAL 47- "IF-ELIF-ELSE" - TICKET PRICES

# age = int(input("Please Enter Your age "))
# if age<=0:
#     print("Not valid, Please Enter a valid Age")
# elif 0<age<=3:
#     print("Ticket Price - Free")
# elif 3<age<=10:
#     print("Ticket price - 150")
# elif 10<age<=60:
#     print("Ticket Price - 250")
# else:
#     print("Ticket Price - 200")
    


# #TUTORIAL 48- "IN" KEYWORD WITH "IF" STATEMENT
# name = input(" Enter your Name ")
# if ('a' or 'A') in name:
#     print("Albhabet is present in " + name)
# else:
#     print("Not present")


#TUTORIAL 49 - " CHECK EMPTY OR NOT"



# #TUTORIAL 50- WHILE LOOP
# i=1
# while i<=10:
#     # print(" Hello World " + str(i))
#     print(f" Hello world {i}")
#     i = i+1

# TUTORIAL 51- ADD 10 NUMBERS USING WHILE LOOP
#sum to 1 to 10
# total=0
# start, End = input("Enter the start and End numbers ").split()
# start = int(start)
# End = int(End)
# while start<=End:
#     total= total+start 
#     start=start+1
# print(total) 


# tutorial 52- exercise
# start, end = input("Enter the start and end value   ").split()
# start=int(start)
# end= int(end)
# total =0
# while start<=end:
#     total= total+start
#     start= start+1

# total = str(total)
# print(f"Total Value is " + total.center(len(total)+2,"*"))


# tutorial 53,54 - 2nd exercise- input 1234 = output 1+2+3+4= 10
# example =("Enter the value of more then 2 digit")
# i=0
# total=0
# while i<len(example) :
    
#     total += int(example[i])
#     i=i+1

# print(f"The ans is : " + str(total))



#tutorial 56,57 

# name= input("Enter your name ")        #kaushal

# i=0
# temp= ""
# while i<len(name):
#     if name[i] not in temp:
#         temp += name[i]
#         print(f" {name[i]} : {name.count(name[i])}")
#     i=i+1


# TUTORIAL 59 - "FOR" LOOP -  10 TIMES HELLO WORLD 
# for i in range (1,11) :
#     print("hello world " +  str(i))


#TUTORIAL 60 - USING "FOR" LOOP - ADDITION OF 1 TO 10

# i,j = input(" Enter the first and last number ").split()
# i= int(i)
# j= int(j)
# total= 0

# for i in range (i, j+1) :
#     total += i 
# print("Total is " + str(total))


#TUTORIAL 66- "DRY"- DONT REPEAT YOUR SELF PRINCIPAL 

# dont write the same code twice

#TUTORIAL 67- STEP ARGUMENT IN FOR LOOP

# i, j = input("Enter the Max and Min value ").split()
# i= int(i)
# j= int(j)
# for i in range (i, j-1, -1) :
#     print(str(i) +", ")
    
#     i-=1


#TUTORIAL 68 - USE OF "STRINGS" IN "FOR" LOOP
# INPUT = 1234, OUTPUT = 1+2+3+4 = 10

# num= input("Enter the number ")  #1234
# total=0                             # i=0
# for i in num :                      # while i< len(num) 
#     total+= int(i)                  # total+= num[i]
# print(total)                        # i+= 1

#TUTORIAL 69 - SUMMARY OF 3RD CHAPTER
# if STATEMENT
# ELIF STATMENT
# "AND"  "OR"
# "WHILE" LOOP
# "FOR" LOOP
# "BREAK" AND "COUNTINUE" KEYWORDS
# "STRING" IN "FOR" LOOP

                                                                                                        #CH-4- TUTORIAL 70 - "FUNCTIONS" - "DEF" AND "RETURN"

#TUTORIAL 71- "PRINT" AND "RETURN" 

# def add_three(a,b,c) :  # MAKE A FUNCTION CALLED ADD_THREE
#      return (a+b+c)
 
# sum= add_three(5,5,5)   # CALLING ADD_THREE FUNCTION
# print(sum)                  


#TUTORIAL 72- MAKE A FUNCION, WHICH GIVE THE LAST CHARACTOR OF INPUT AS OUTPUT
# def last_char (string) :
#      return (string[-1])

# name=input("Enter your name ")
# print(f"Total lenth of the name is {len(name)} and last char is {last_char(name)}")


# 2ND PROGRAM- ODD AND EVEN
# def odd_even(num) :
#     if num%2 == 0 :
#         return "Even number"
#     else:
#         return "Odd number"


# num= input("Enter the number ")
# num=int(num)
# print(odd_even(num))


#TUTORIAL 73,74- EXERCISE- FIND GRATER NUMBER IN 2
# def grater_num(a,b) :
#     if a>b :
#         return a
#     return b

# a,b= input("Enter two numbers ").split()
# print(grater_num(a,b) +" is grater")


# TUTORIAL -75 - FIND GRATER IN 3 NUMBERS

# def grater_three(a,b,c) :
#     if a>b and a>c :
#         return a
#     elif b>a and b>c :
#         return b
#     return c

# a,b,c = input("Enter 3 numbers ").split()
# print(grater_three(a,b,c) + " is grater")

# TUTORIAL - 76 - "FUNCTION" INSIDE "FUNCTION" -NESTED
# def grater(a,b) :
#     if a>b :
#         return a
#     else :
#         return b

# def nested_grater(a,b,c) :
#     bigger= grater(a,b)
#     return grater(bigger,c)

# a,b,c = input("Enter three numbers ").split()
# print(nested_grater(a,b,c))


#TUTORIAL -77,78 - EXERCISE AND SOLUTION 

# def is_palindrom(word) :
    
#     if word == word[::-1] :
#         return "Palindrom"
    
#     return "Not palindrom"

# name = input("Enter the name to check ")
# print(is_palindrom(name))

#tutorial 79- fibonacci series



                                                                                                                                 #TUTORIAL -82 CH-5 "LIST"
# WE CAN STORE DIFFRENT DATAS IN LIST- INT,FLOAT,STRINGS, MIX DATA

# number= [1,2,3,4]     #list of 4 numbers
# print(number)

# list= ["word1", "word2", "word3", "word4"]   #use "" or '' for strings
# print(list)

# mix=[1, "word", 2.3, 4.0]
# print(mix)

# for i in range (1, 11) :
#     print(i,  end=", ")                     #used to print output in same line

#tutorial 83- append(a) mathod- it takes only 1 argument

# fruits= ['grapes', 'apple']
# fruits.append('mango')
# print(fruits)

# fruits=[]
# a,b= input('Enter the names of 2 fruits ').split()
# fruits.append(a,b)                     # 
# print(fruits)

#tutorial-84 - Methods to add data like:-insert, extend, append,
# 
# 

# tutorial 85- methods to delete data from lists
# like: pop(index), del , remove("string") 

#tutorial 86- "In" in lists


# tutorial 87- other methods in list
# COUNT('') METHOD, SORT() METHOD, SORTED FUNCTION, REVERSE, CLEAR, COPY

# fruits= ['apple', 'bnana', 'grapes', 'orange', 'mango','apple']

# # print(fruits.count('apple'))

# fruits.sort()           # sort method make the list sort for ever
# print(fruits)

# print(sorted(fruits))   # sorted is just print the list in sorted order

# # fruits.clear()
# # print(fruits)           # no data will show, because data is cleared

# copyed_list= fruits.copy()
# print(copyed_list)


# tutorial 88- diffrence b/w  "==" and "is" in list
# both used to compaire the list

# fruits1=['apple', 'mango', 'grapes', 'orange']
# fruits2=['apple', 'mango', 'grapes', 'orange']

# print(fruits1==fruits2)            # == checks the values/objects are same or not
# print(fruits1 is fruits2)          # 'is' checks the memory location is same or not


#tutorial 89- join and split method 


#tutorial 90

#tutorial 91- string vs list

#tutorail 92- looping in list
# matrix= [1,2,3,4,5,6,7]

# for i in matrix:
#     # print(i)
#     print(i, end= " ")

#tutorial 94- more about list

#tutorial 95,96 exercise
# input list[1,2,3,4] =  output square [1,2,9,16]

# def square (l):                      
#     sq= []
#     for i in l:
#         sq.append(i**2)
#     return sq


# list= [1, 2, 3]
# print(square(list))

# tutorial 97,98- exercise 2
#  1,2,3,4 - 4,3,2,1

# def reverse(l):
#     # return l[::-1]               #type 1, by [::-1]
#     rev=[]
#     i=1
#     while i<=len(l) :
#         rev.append(l.pop()) 
#     return rev 

# list= [1, 2, 3, 4, 5]
# print(reverse(list))

#tutorial 99,100 -exercise 3
# input ['abc', 'def', 'ghi']  = out['cba', 'fed', 'ihg']

# def reverse(l) :
#     ele = []
#     for i in l:
#         ele.append(i[::-1])
#     return ele
    
# list= ['abc', 'def', 'ghi']
# print(reverse(list))

#tutorial 101- odd/even

# def odd_even(l):
#     odd=[]
#     even=[]
#     combine=[]
#     for i in l:
#         if i%2==0 :
#             even.append(i)
#         else :
#             odd.append(i)

#     combine = [odd, even]
#     return combine


# numbers=[1, 2, 3, 4, 5, 6, 7]
# print(odd_even(numbers))


#tutorial 102- common numbers in 2 list
'''
def common(l1, l2) :
    com=[]
    for i in l1 :
        j=0
        while j<len(l2) :
            if i == l2[j] :
                com.append(i)
                j=j+1
    return com

i,j = input("enter the first and last number for list 1 ").split()
m,n = input("enter the first and last number for list 2 ").split()
i = int(i)
j = int(j)
m = int(m)
n = int(n)
l1 = list(range(i, j+1)) 
l2 = list(range(m, n+1))
print(l1, l2)

print(common(l1, l2))
   '''

                                                                                                                    # CH-9  LIST COMPREHENSION 
# EXAMP: MAKE A FUCTION FOR SQUARE IN LIST 

# # simple way:
def square(n):
    sq=[]
    for i in n:
        sq.append(i**2)
    return sq
     

list1=[]
number= int(input("Enter the length of the list "))
print("Enter the values in list ")
for i in range(number):
    list1.append(int(input()))

print("The squares of the numbers are ", end= " ")
print(square(list1))




                                                                                                # CH-10 -  Dictonery comprehension - tutorial 137
# output = {1:1, 2:4, 3:9, 4:16}
# square= {num: num**2 for num in range(1,11)}
# print(square)

# number= int(input("Enter the lenth for the sqaure series "))
# square = {f"Square of {num} is": num**2 for num in range(1, number+1)}
# print(square)

# Example -2  

# string= input("Enter the name ")
# Word_count = { char: string.count(char) for char in string }
# print(Word_count)

# tutorail 138- odd_even in directory
# output= ('1: odd', '2: even', --)
# min,max= input("Enter the start and end values ").split()
# min= int(min)
# max= int(max)
# odd_even= {i: ('even'if i%2==0 else 'odd') for i in range(min,max+1)}
# print(odd_even)

                                                                                                    # chap-11 tutorial 140 - * args -very important
# * args is a tuple

# def add_all (*args) :
#     total=0
#     for num in args:
#         total= total+num
#     return total

 
# # number= input("Enter the numbers to add ")
# number=(1,2,3,4,5)
# print(add_all(*number)) 


# tutorial 143 - Exercies 1

# def power (pow, *args):
#     if args:
#         result=[i**pow for i in args]
#         return result
#     else: 
#         return "You have not pass any value"


# # list1 =input("Enter the values of list ")
# # print(power(pow, *list1))
# pow= int(input("Enter the value of power "))
# list= [1,2,3]
# print(power(pow,*list))


# tutorial 145 - **kwargs
# **kwargs is a Dictonery {}

def demo(**kwargs):
    print(kwargs)

d={'name':'kaushal', 'age':'27'}
demo(**d)

