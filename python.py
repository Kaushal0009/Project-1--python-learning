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
'''a= int(input("Enter the number "))
f=0
c=1
while(c<a+1):
    if(a%c==0):
        f=f+1
    c=c+1
if(f==2):
    print(a, "is Prime number")
   '''

''' 
a= int(input("Enter the number "))
c=0
while(a>0):  
    c=c*10+(a%10) 
    a=int(a/10)
print(c)
'''

'''a= input("Enter the number ")
f=0
c=0
for i in a:
    f=f+1
print("total digits in the number is ",f)

a=int(a)
for j in range(1,f+1):
    c=c*10+(a%10)
    a=int(a/10)
print(c)
   '''    
'''
a= int(input("Enter the number "))
f=0
c=0
for i in range(1,int(a/2)):
    f=a%i 
    if(f==0):
        c=c+1
if(c==1):
    print(a, "is a prime number")
else:
    print(a, "is not a prime number")
'''

'''a= input("Choose the alphabet ")
while (a!="z"):
    print(a)
    a= input("Choose the alphabet again")    
print ("Game over")
'''

'''a= int(input("Choose the Number "))
for i in range(1,a+1):
    if(i%2==0):
        print(i)
'''


'''
a= int(input("Choose the Number "))
sum =a%10
while(a>10):
    a=a//10
sum=sum+a
print(sum)
'''    
'''
n= int(input("Choose the Number "))
a = 0
b = 1
if n == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)
'''

'''a= int(input("Choose the Number "))
i=0
while(a>0):
    i= i*10+a%10
    a= int(a/10)
if (a=i):
    print(p)
'''
'''
a= int(input("Choose the Number "))
for i in range(a+1):
    for j in range(a-i):
        print("*", end= " ")
    print("\n")
'''

'''a= int(input("Choose the Number "))

for i in range(a+1):
    for j in range(1,i):
        print(j, end= " ")
    print("\n")
'''
'''
a= int(input("Choose the Number "))

for i in range(0,a):
    for k in range(i):
        print(end=" ")                                 #1234
    for j in range(i+1,a+1):
        
        print(j, end= " ")
    print("\n")
'''
'''
a= int(input("Choose the Number "))
for i in range(0,a):
    for k in range(i,int(a/2)+2):
        print(end=" ")                                 #1234
    for j in range(i+1):
        
        print("*", end= " ")
    print("\n")
'''
a= int(input("Choose the Number "))
sum=0
for i in range(1,a+1):
    k=1
    print(i)                                 #1234
    for j in range(1,i+1): 
        k= k*j   
    print('k',k)
    sum=sum+k
print(sum)
    
