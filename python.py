                                                    # 1- IF STATEMENTS' USE
'''
a= int(input("Enter Number 1  "))
b= int(input("Enter a Number 2  "))
if (a%2 == 0):
    print('Even number')

else:
    print("Odd number")


if(a>b):
    print("A is grater")
else:

    print("B is grater")
'''

                                                # 2- IF-ELIF STATEMENTS' USE
'''
a= int(input("Enter Number  "))
if(a==0):
    print("The input is 0")
elif(a>0):
    print("Positive Number")
else:
    print("Negitive number")
'''
'''
a= int(input("Enter Number  "))
if(a%5==0 and a%11==0):
    print("Divisible by both 5 & 11")
elif(a%5==0):
    print("only divisible by 5")
else:
    print("Only divisible by 11")
'''
'''a= int(input("Enter Your Marks  "))
if(a<33):
    print("You are fail")
elif( a>33 and a<=50):
    print("Grade c")
elif( a>50 and a<=70):
    print("Grade B")
elif( a>70 and a<=85):
    print("Grade A")
else:
    print("Marit list")
'''

'''
one ='jan' 
Two = 'Feb' 
Three ='Mar'
Four ='April'
Five='May'
a= input("Enter the Month Number  ")
if a=='one' or a=='One':
    print("You have selected",one, "Month and it has 31 days")
elif a=='Two' or a=='two':
    print("You have selected",Two, "Month and it has 28 days")
'''
                                             # FOR LOOP IN PYTHON
'''
a = int(input("Enter the number"))

for i in range (1,a+1):
    print(i)
'''



'''
a = int(input("Enter the salary"))
Total = 0
DA = 0
HRA = 0


if (a<=0):
    print("Invalid Value")

elif(a>10000 and a<20000):
    DA = (a/100)*90
    HRA = (a/100)*25
    Total = a+DA+HRA
    print("Your gross salary is ", Total)

elif (a>0 and a<10000):
    DA = (a/100)*80
    HRA = (a/100)*20
    Total = a+DA+HRA
    print("Your gross salary is ", Total)

else:
    DA = (a/100)*95
    HRA = (a/100)*30
    Total = a+DA+HRA
    print("Your gross salary is ", Total)



'''                                                         #WHILE LOOP
'''
a= 1
while(a<=10):
    if(a==7):
        pass        
    print(a)
    a=a+1

'''
'''                                        
a= int(input("Enter the number "))
f=1
while(a>0):
    f=f*a
    a=a-1
print(f)
'''
'''
a= int(input("Enter the number "))
f=0
while(a!=0):
    f=f+1
    a=int(a/10)
print(f)
'''
a= int(input("Enter the number "))
f=0
c=1
while(c<a+1):
    if(a%c==0):
        f=f+1
    c=c+1
if(f==2):
    print(a, "is Prime number")
    




    

