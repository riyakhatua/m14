'''
print(float(4),float('4.5'))
print(float(True))
'''
#complex
'''
c1,c2=4+34j,3.4-45.7j
print(c1,c2)

a=4,5
print(a)
'''

#constructor
#1
'''
print(complex())
'''
#2.typecasting
#int-->complex
'''
print(complex(45),complex(45j))
'''
#float-->complex
'''
print(complex(45.6),complex(45.6))
'''
#bool-->complex
'''
print(complex(True))
'''
#string-->complex
'''
print(complex('90'),
      complex('4.5'),
      complex('4j'))
'''    
#program to check operator used in complex
'''
i1=complex(input("Enter 1st num:"))
i2=complex(input("Enter 2nd num:"))
print("Addition:",i1+i2)
print("sub:",i1-i2)
print("mul:",i1*i2)
print("div:",i1/i2)
print("mod:",i1%i2)
print("exoi:",i1**i2)
'''
#4.boolean
'''
b1,b2=True,False
print(b1,b2)
print(type(b2))
#constructor
#1.
print(bool())
'''
#note
'''
print(bool(0),bool(34))
print(bool(0.0),bool(34.2))
print(bool(0j),bool(34+3j))
print(bool(False),bool(True))
'''

#user input
'''
i=bool(input("Enter:"))
print(i,type(i))

i=bool(int(input("Enter:")))
print(i,type(i))

i=bool(float(input("Enter:")))
print(i,type(i))

i=bool(complex(input("Enter:")))
print(i,type(i))
'''
#9.isinstance
'''
print(isinstance(34,int))
print(isinstance('a',int))
print(isinstance(3.4,float))
print(isinstance(34-4j,
                 (int,complex)))
print(isinstance(True,
                 (int,complex)))
print(isinstance(6.7,
                 (int,complex)))
'''
#10.abs
'''
print(abs(-34))
print(abs(3.4))
'''
#11.trunc
'''
import math
print(math.trunc(3.4))
print(math.trunc(51.65))
print(math.trunc(3.9))
'''
#divmod
'''
n1=45
n2=5
print('division',n1/n2)
print('division',n1//n2)
'''
#typecasting
'''
i,f,c=str(34),str(34),str(3+4j)
print(type(i),i)
print(type(f),f)
print(type(c),c)
'''
#to know number of character
'''
s_=input("Enter a string:")
print("string:",s_,
      "It is length is",len(s_))
'''
'''
str1="B@ng@!oR3"
print(id(str1))
print(str1,len(str1))
#starting character
print(str1[0],str1[-9],str1[-len(str1)])
'''
#ending character
'''
print(str1[8],str1[-1],str1[len(str1)-1])
print(id(str1[1]),id(str1[4]))
'''
#middle character
'''
print(str1[4],str1[-5],str1[len(str1)-5])
'''
#character of any string
'''
str1="B@ng@!or3"
middle_index=len(str1)//2
print(middle_index, str1[middle_index])
'''
'''
str1=input("enter:")
middle_index = len(str1)//2
print(middle_index,str1[middle_index])
'''
#slicing
'''
s2= "it's cold here"
print(len(s2))
print(s2,s2[::],s2[0:len(s2):1])
#it's
print(s2[0:4:1],s2[:4:],s2[-len(s2):-10:])
#here
print(s2[10::],s2[-4::])
#cold
print(s2[5:9:],s2[-9:-5:])
'''
#for reverse
s2 ="welcome to my channel :)"
'''
print(s2[::-1])
print(s2[len(s2):-len(s2)-1:-1])
print(s2[len(s2):-25:-1])
'''
#channel
#for positive
'''
print(s2[20:13:-1])
'''
#for negative
'''
print(s2[-4:-11:-1])
'''
#welcome to
'''
#for positive
print(s2[9::-1])
#for negative
print(s2[-15:-25:-1])
#to my
#for positive
print(s2[12:7:-1])
#for positive
print(s2[-12:-17:-1])
'''
str1="slicing is tricky"
#ing is tr
print(str1[12:3:-1])
print(str1[len(str1):-18:-1])


























      


