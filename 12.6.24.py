#isidentifier
print('num1'.isidentifier())
print('9a'.isidentifier())
print('a_1'.isidentifier())
print('_1a'.isidentifier())
print('a_'.isidentifier())
print('a+'.isidentifier())

#divmod
n1=45
n2=5
print('division',n1/n2)
print('division',n1//n2)
print('division',n1%n2)
print(divmod(n1,n2))

#integer
'''
a,b=10,-9
print(a,b)
print(type(a))
'''

#integer
a,b=10,-9
print(a,b)
print(type(a))
#constructor
print(int())
#typecast
#float-->int
#str(numbers)-->int
#bool-->int
print(int(4.5),int('4'))
print(int(False),int(True))

#exception
'''
print(int('4a'))
print(int(4+4j))
print(int('4.5))
'''

#user input
'''
num=input("enter a num:")
print(num,type(num))

num=int(input("enter a num:")
print(num,type(num)
'''

#float
f1,f2=45.5,-4.5
print(f1,f2)
print(type(f2))
#constructor
#1.
print(float())
#2.
print(float(4),float('45'))
print(float(True))

#exception
print(float(4+5j))
print(float('4.5a'))

#use input
f1=float(input("Enter a number:"))
print(f1,type(f1))

#operators
f1=float(input("Enter 1st num:"))
f2=float(input("Enter 2nd num:"))
print("Addiyion:",f1+f2)
print("sub:",f1-f2)
print("mul:",f1*f2)



