#with variable
'''
n1=25
n2=40
print(n1,n2)
temp=n1
n1=n2
n2=temp
print(n1,n2)
'''
#without variable
'''
n1=20
n2=40
print(n1,n2)
n1,n2=n2,n1
print(n1,n2)
'''
#operators used in complex
'''
i1=complex(input("Enter 1st num:"))
i2=complex(input("Enter 2nd num:"))
print("Addition:",i1+i2)
print("sub:",i1-i2)
print("mul:",i1*i2)
print("div:",i1/i2)
print("mod:",i1%i2)
print("floor-div:",i1//i2)
print("expo:",i1*i2)
'''
#print
'''
x,y,z=20,40,60
print(x,y,z)
print(x,y,sep=',')
print(z,x,sep=',')
print(y,z,x,sep='5')
print(y,z,x,sep='-')
print(x,y,z,sep='a')
'''

#string
'''
s1,s2='hii guys!',"how was your weekend?"
print(s1,s2,sep='\n')
s3='''
('Hey whatsup')
'''
print(s3)
s4="""welcome to Jspider
Pyspider & Qspider"""
print(s4)
#constructor
#1
'print(str())'
'''

#typecasting
'''
i,f,c=str(34),str(3.4),str(3+4j)
print(type(i),i)
print(type(f),f)
print(type(c),c)
'''
#to know number of character
'''
s_=input("Enter a string:")
print("string:",s_,
      "It is length is:",len(s_))
      '''
#index character
'''
str1="B@ng@!0R3"
print(id(str1))
print(str1,len(str1))
#indexing
#starting character
print(str1[0],str1[-9],str1[-len(str1)])
#ending character
print(str1[8],str1[-1],str1[len(str1)-1])
#middle character
print(str1[4],str1[len(str1)-5],str1[-5])
'''

#character of any string
'''
str1="B@ng@!0r3"
middle_index=len(str1)//2
print(middle_index,str1[middle_index])


#last 2nd character print

str1=input("Enter a string:")
last_second=len(str1)-2
print(str1[last_second])
#2
print(str1[-2])
'''

#slicing
'''
s1="it's cold here"
print(s1,s1[::],s1[0:len(s1):1])
print(len(s1))

#it's
print(s1[0:4:1],s1[:4:],s1[-len(s1):-10:])

#here
print(s1[-4::],s1[10::])

#cold
print(s1[5:9:],s1[-9:-5])
'''
#when step value is more than 5
'''
s3="welcome to my channel :)"

print(s3)
'''
#character in even index
'''
print(s3[0:len(s3):2])
'''
#character in odd index
'''
print(s3[1::2])
'''
#welcome
'''
print(s3[:7:])
#welcome skip odd index char
print(s3[:7:2])
#welcome skip even index char
print(s3[1:7:2])
'''
#reversing the strin
''''
s4="welcome to my channel :)"

#welcome to
#for positive
print(s4[9: :-1])
#for negative
print(s4[len(s4)-15:-25:-1])

#to my
#for positive
print(s4[12:7:-1])
#for negative
print(s4[len(s4)-12:-17:-1])
'''
#reverse
''''
m1="slicing is tricky"
#ing is tr
print(m1[12:3:-1])
#negative
print(m1[-5:-14:-1])

#for slicing
print(m1[6::-1])
#negative
print(m1[-11:-18:-1])
'''
'''
s3="welcome to my channel :)"
print(s3[::-1])
#channel
#for positive
print(s3[20:13:-1])
#for negative
print(s3[-4:-11:-1])
'''
'''
print(int(4.5),int(4))
print(int(True),int(True))
a=4,5
print(a)
'''

#convention for variable
'''
mynameis = 'Riya'
print(mynameis)
'''
#pascal case--> classname
'''
MyNameIs = 'Riya'
print(MyNameIs)
'''
#camel case --> methodname
'''
myNameIs = 'Riya'
print(myNameIs)
'''
#snake case --> functionname
'''
my_name_is = 'Riya'
print(my_name_is)
'''
'''
str2='welcome to my channel'
print(str2[::-1])
#reverse the string and
#skip odd index character
print(str2[-1::-2])
#reverse the string and
#skip even index character
print(str2[-2::-2])
#welcome-->reverse and skip odd index
print(str2[-15::-2])
#to my->reverse and skip even index
print(str2[-8:-14:-2])
'''
'''
s5='laptop@1'
print(s5[:3:])
print(s5[-6:-9:-1])
print(s5[1::2])
print(s5[::-2])
'''
#string is immutable
'''
str4 = 'Hai'
str4[0] = 'h'
print(str4)
'''
#method in string
#1. Replacement
'''
str1 = 'hello world'
print(str1.replace('l', 'L'))
print(str1.replace('hello', 'hai'))
print(str1.replace('l', 'L', 1))
print(str1.replace('o', '@', 2))
str2='hello world hello'
print(str2.replace('hello', 'hai'))
print(str2.replace('o', '@', 2))
'''
#2. lower
'''
s_2 = input("Enter the string: \n")
print(s_2.lower())
'''
#3. upper
'''
s_2= input("Enter the string : \n")
print(s_2.upper())
'''
#4. swap case
'''
s_2=input("Enter the string : \n")
print(s_2.swapcase())
'''
#5.islower
'''
s_2 = input("Enter the string : \n")
print(s_2.islower())
'''
#6.isupper
'''
s_2 = input("Enter the string :\n")
print(s_2.isupper())
'''
#7.isalphabet
'''
s_2 = input("Enter the string :\n")
print(s_2.isalpha())
'''
#8.isnumeric
'''
s_2 = input("Enter the string ; \n")
print(s_2.isnumeric())
'''
#9.isalnum
'''
s_2 = input("Enter the string ; \n")
print(s_2.isalnum())
'''
#10.isspace
'''
s_2 = ''
print(s_2.isspace())
s_3 =' '
print(s_3.isspace())
s_3 = 'hai 56'
print(s_3.isspace())
'''
#11.startswith
'''
str1=input("enter:")
sub_s=input("substring:")
print(str1.startswith(sub_s,0,len(str1)))
sub_s=input("substring:")
start_value=int(input("start-index:"))
print(str1.startswith(sub_s,start-value))
'''            
#12.endswith
'''
str1 = input("enter : \n")
sub_s = input("substring: \n")
print(str1.endswith(sub_s))
sub_s = input("substring: ")
end_value = int(input("end-index : "))
print(str1.endswith(sub_s, 0, end_value))
'''
#13.split
'''
str3 = "welcome to bangalore"
print(str3.split())

str3 = "welcome to-bangalore"
print(str3.split())
'''
#sep
'''
str3 = "welcome-to-bangalore"
print(str3.split('-'))
print(str3.split('to'))
print(str3.split('a'))
'''
#maxsplit
'''
str3 = "welcome-to-bangalore -"
print(str3.split('o'))
print(str3.split('o',1))
print(str3.split(' ',2))
'''
#14.rsplit
'''
str3 = "welcome to bengalore"
print(str3.rsplit())
str3 = "welcome-to -bengalore"
print(str3.rsplit())
'''
'''
n=input("enter:")
print(n,type(n))
'''
'''
n1=input("enter:")
n2=input("enter:")
print(n1+n2)
'''
#15.index
'''
str1 = input("enter : ")
sub_s = input("enter the sub_s :\n")
print(str1.index(sub_s))
sub_string = input("enter the sub_s :\n")
str_index = int(input())
print(str1.index(sub_string, str_index))
'''
#16.find
'''
str1 = input("enter : ")
sub_s = input("enter the sub_s :\n")
print(str1.find(sub_s))
sub_string = input("enter the sub_s :\n")
str_index = int(input())
print(str1.find(sub_string, str_index))
'''
#exception
'''
str1=input("enter:")
sub_s = input("enter the sub_string:")
print(str1.find(sub_s))
'''
#17.count
'''
str1= "Good morning maam"
print(str1.count('o'))
print(str1.count('Good'))
print(str1.count('a'))
print(str1.count('m'))
print(str1.count('123'))
print(str1.count('o',2))
'''
#to remove character from string
#18. strip
'''
str1 = input("enter : ")
char_= input("enter : ")
print(str1.strip(char_))
'''
#19.lstrip
'''
str1 = input("enter: ")
char_= input("enter : ")
print(str1.lstrip(char_))
'''
#20. rstrip
'''
str1 = input("enter: ")
char_= input("enter : ")
print(str1.rstrip(char_))
'''
#21.join
'''
l_=["a", 'b', "7"]
print(''.join(l_))
#combine
print('-'.join(l_))
print('8'.join(l_))
print('i'.join(l_))
'''
#for tuple
'''
t_ = ("a", 'b', "7", 'apple', '6')
print(''.join(t_))
'''
#for set
'''
s_ ={"a", 'b', "7", 'apple', '6'}
print('-'.join(s_))
'''
#for dict
'''
d_ ={"a":8, 'b': 4.5, "7": 34}
print('@'.join(d_))
'''
#for string
'''
str_ = 'hello'
print('-'.join(str_))
'''
#operators in string
'''
str_1 = input("enter :")
str_2 = input("enter :")
print(str_1+str_2)
print(str_1*2)
'''
'''
count_=int(input("enter :"))
print(str_1*count_)
print(*str_2)
'''
#2.list
#homogeneous
'''
list1 = [23, 45, 12, 895, 34, 23]
print(list1)
'''
#heterogeneous
'''
list2 = ['23', [45, 12, 895], 34.5, 23, 3+6j, False, 0]
print(list2)
print("length of list : \n",
      len(list2))
print(type(list2))
'''
#constructor
#default value
'''
print(list())
'''
#typecasting
#string to list
#according to character
'''
print(list('bangalore is in karn'))
#according to words
print('bangalore is in karn'.split())

#tuple into list
print(list(('bangalore', 34, 4.5)))

#set into list
print(list({'bangalore', 34, 4.5}))

#dictionary into list
print(list({'bangalore': 45, 34: 45, 4.5: True}))
'''
'''
list2 = ['23', [45,12, '895'],
         34.5, 23, 3+6j, False,
         0]
         '''
#indexing
'''
print(list2[0])
print(list2[len(list2)-2])
print(list2[-6], list2[1])
print(list2[1][1], list2[-6][-2])
print(list2[1][2], list2[-6][-1])
print(list2[1][2][1],
      list2[-6][-1][-2])
'''
#program to get even index element
'''
print(list2[0:len(list2):2])
'''
#program to get odd index element
'''
print(list2[1:len(list2):2])
'''
#program to reverse the list
'''
print(list2[::-1])
'''
#program to get even index element in reverse order
'''
print(list2[::-1])
'''
#[23, 3+6j, False, 0]
'''
print(list2[3:len(list2)])
print(list2[:-5:-1])
'''
#[23, False]
'''
print(list2[-2:-5:-2])
'''
#[False,23]
'''
print(list2[3::2])
'''
#list is immutable
'''
str = 'hello'
str_1 = 'E'
print(str)
'''
#indexing
'''
li2 = [45, 3.5, 2.3, 'hey',
       [True, False]]
li2[-2] = "HEY"
print(li2)
'''
#slicing
'''
li2 =  [45, 3.5, 2.3, 'hey',
       [True, False]]
li2[0:2] = [34, 67
'''
#method in list                              #24/06/24
#1.adding element into the list
#append
'''
list1 = [34.5,"riya", [1,2,3,4], [True]]
list1.append("hai")
list1.append([43, 52, "56"])
print(list1)
'''
#extend: unpacked
'''
list1 = [34.5,"riya", [1,2,3,4], [True]]
list1.extend("hai")
list1.extend(["hai", 435, False, 5.6])
list1.extend("hai")
print(list1)
'''
#insert at specific position
'''
list1 = [34.5,"riya", [1,2,3,4], [True]]
list1.insert(0, 'bangalore')
list1.insert(4, "74r8")
list1.insert(2, 78)
print(list1)
'''
#removing elements from the list
#pop
'''
l2 = [56,31, 78, 21, 89, 89, 56]
l2.pop()
l2.pop(2)
print(l2)
'''
#remove
'''
l2 = [56,31, 78, 21, 89, 89, 56]
l2.remove(31)
l2.remove(56)
print(l2)
'''
#delete
'''
l2 = [56, 31, 78, 21, 89, 56]
del l2[0]
del l2[1]
del l2[-1]
print(l2)
'''
#reverse
'''
l2 = [56, 31, 78, 21, 89, 56]
print(l2[::-1])
l2.reverse()
print(l2)
'''
#indexing
'''
l2 = [56, 31, 78, 21, 89, 56]
print(l2.index(31))
print(l2.index(21))

'''

#slicing
'''
l2 = [56, 31, 78, 21, 89, 89, 56]
del l2[:2]
print(l2)
del l2[2:5]
print(l2)
del l2[::2]
print(l2)
del l2[1::2]
print(l2)
'''

#reverse
'''
l2 = ['a', 45, 4.5, [4,3], True]
print(l2[::-1])
l2.reverse()
print(l2)
'''
#indexing
'''
l2 = ['a', 45, 0, 4.5, [4,3], True, 1, False]
print(l2.index(False))
print(l2.index(False, 3))
print(l2.index('a'))
print(l2.index(1))
print(l2.index(45))
'''
#count
'''
l2 =['a', 45, 0, 4.5, [4,3], True, 1, False]
print(l2.count('a'))
print(l2.count(True))
print(l2.count([3.4]))
'''
#sort                                          #25/06/24
'''
list_ =[3,4,12,78,4.5,78,0,1]
list_.sort()
print(list_)
list_.sort(reverse=False)
print(list_)
list_.sort(reverse=True)
print(list_)
'''
'''
list_=['apple', "Apple", 'grapes',
       'van', 'wayanad', 'IN', "avacado"]
list_.sort()
print(list_)
'''
'''
l_=["3+4j", "4+5j", "1+6j"]
l_.sort()
print(l_)
'''
'''
l_1=[True, False]
l_.sort()
print(l_1)
'''
#copying the list
#1. normal copy
'''
li_=['apple', "Apple", ['grapes',
       'van', 'wayanad'], 'IN', "avacado"]
li_1=li_
print(li_)
print(li_1)
print(id(li_), id(li_1))
print(id(li_[2]), id(li_1[2]))
'''
#shallow copy
'''
li_=['apple', "Apple", ['grapes',
       'van', 'wayanad'], 'IN', "avacado"]
li_ = li_.copy(li)
print(li_1)
print(id(li_), id(li_1))
print(id(li_[2]), id(li_1[2]))
'''
#3. deep copy
'''
from copy import deepcopy
li_=['apple', "Apple", ['grapes',
       'van', 'wayanad'], 'IN', "avacado"]
li_1 = deepcopy(li_)
print(li_1)
print(id(li_), id(li_1))
print(id(li_[2]), id(li_1[2]))
'''
#operators in list
'+'
'*'
#ord and chr
'''
print(ord('t'), ord('1'), ord('&'))
print(chr(65), chr(100), chr(32), chr(2))
'''
#tuple
'''
t_ = (45, 7, 'apple', (4,5), [2.5, 3])
print(t_)
print(type(t_))
'''
#single value tuple
'''
t_1= (45,)
print(t_1, (t_1))
'''
#constructor
'''
print(tuple())
print(tuple('python',),
            tuple([4, 5.3, True]),
            tuple({'a', 'b', 'c'}),
            tuple({3: 45, False: 45}))
 '''           
#program to check indexing and slicing in tuple      #26/06/24
#indexing in tuple
'''
tuple = "she is a good girl"
print(len(tuple))
print(tuple[0],tuple[-18],tuple[-len(t_)])
'''
'''
t_ = ('apple', 'orange', 'guava', 23, 45)
print(t_[0])
print(t_[-2])
'''

#slicing in tuple
'''
t_ = (34.5, "riya", [1,2,3,4], [True])
print(t_[1:])
print(t_[:1])
print(t_[::])
print(t_[::-1])
print(t_[1:2:1])
'''
#operator in tuple
#'+'
#'*'
'''
t_ = ("45")
t1_ =("45")
print(t_+t1_)
print(t_*2)

tuple1 = (1, 2, 3)
tuple2 = ('python', 'apple')
print(tuple1+tuple2)
print(tuple1*2)
'''
#method in tuple
#count
'''
t_= (3, 4, 2.3, 'apple', (4,), 3.0)
print(t_.count(3))
print(t_.count('Apple'))
'''
#index
'''
t_= (3, 4, 2.3, 'apple', (4,), 3.0)
print(t_.index(2.3))
print(t_.index(3))
print(t_.index(3,1))
print(t_.index("apple"))
'''
#tuple is immutable
'''
t_= (3, 4, 2.3, 'apple', (4,), 3.0)
t_[-1] =4.7
print(t_)
'''




#'count'
#'index'

#convert the string into , seperated string
'''
str1 = "she is a good girl"
print(str1.split())                     
'''
#difference between find and index          #index give error, find give -1
'''
str1 = input("enter : ")
sub_s = input("enter the sub_s :\n")
print(str1.find(sub_s))
sub_string = input("enter the sub_s :\n")
str_index = int(input())
print(str1.find(sub_string, str_index))
'''
'''
str1 = input("enter : ")
sub_s = input("enter the sub_s :\n")
print(str1.index(sub_s))
sub_string = input("enter the sub_s :\n")
str_index = int(input())
print(str1.index(sub_string, str_index))
'''
#how to check whether the string is empty
'''
i = ''
print(bool())
'''

#check whether python string is substring of hello welcome to my world
'''
str1=("hello welcome to my world")
sub_s = input("enter the sub_string:")
print(str1.find(sub_s))
'''
#'+'
'''
a=input("a:")
b=input("b:")
print(a+b)
'''
#reverse the string fron user input
'''
str1=input("enter:")
print(str1[::-1])
'''
#immutability of string
'''
s_1 = "hello world"
s_1.upper()
print(s_1)
'''
#list
'''
name = ['apple', 'google', 'amazone', 'facebook', 'instagram',
        'snapchat', 'whatsapp', 'swiggy', 'rapido', 'ola']

name.append('netflix')
name.append('prime')
name.append('hotstar')
print(name)
name.extend('netflix')
name.extend('prime')
name.extend('hotstar')
print(name)
'''
#difference between pop and remove
#pop #It gives indexerror   #remove the element based on index given
'''
l2 = [56,31, 78, 21, 89, 89, 56]
l2.pop()
l2.pop(2)
print(l2)
'''
#remove #gives valueerror  #remove the first matching value from list
'''
l2 = [56,31, 78, 21, 89, 89, 56]
l2.remove(31)
l2.remove(56)
l2.remove(89)
print(l2)
'''
#sort the list in decending order
'''
list_ =[3,4,12,78,78,0,1]
list_.sort()
print(list_)
list_.sort(reverse=True)
print(list_)
'''

#create a list with each character of the string as elements in list
'''
str1="developers in pyspider"
str_=list(str1)
print(str_)

#create a list with each word of the string as its element
str1="developers in pyspider"
print(str1.split())
'''

#hash()                               #27/06/24
'''
print('a'.__hash__())
print(hash((4,5,6)))
print(hash(4.5))
print(hash([True,False]))
'''
#set
'''
set_={'a', (4,), 45, 4.4, 3-4j, False, 'a'}
print(set_)
print(type(set_))
print(set())
print(len(set_))
'''
#typecasting
'''
print(set("hello"))
print(set([3, 4.5, (4,5), (4,)]))
print(set((3, 4.5, (4,5), (4,))))
print(set({'a': 1, 'b': 2, 'c': 3}))
'''

#methods

#1.add
'''
set_=set()
set_.add('riya')
set_.add((3,4))
set_.add(4)
set_.add('rakhi')
print(set_)
'''
#union
'''
set_1 = {'a', (4,), 45, 4.4, 3-4j, False, 'a'}
set_2 = {'a', 'b', 'c'}
set_3 = {4.5, 3+4j, 'kiwi', (9,8)}
print(set_1.union(set_2))
print(set_2.union(set_1, set_3))
'''

#update
'''
set_1 = {'a', (4,), 45, 4.4, 3-4j, False, 'a'}
set_2 = {'a', 'b', 'c'}
set_3 = {4.5, 3+4j, 'kiwi', (9,8)}
set_1.update(set_3)
print(set_1)
set_3.update(set_2, set_1)
set_3.update(set_2, ('abc'))
print(set_3)
set_2.update(set_2)
print(set_2)
'''

#removing a key from the set
#pop
'''
set_1 = {'a', (4,), 45, 4.4, 3-4j, 67, 'a'}
set_1.pop()
print(set_1.pop())
print(set_1)
'''
#remove
'''
set_1 = {'a', (4,), 45, 4.4, 3-4j, False, 'a', 23}
set_1.remove((4,))
print(set_1)
#keyerror
set_1.remove(23)
print(set_1)
'''
#discard
'''
set_1 = {'a', (4,), 45, 4.4, 3-4j, False, 'a', 23}
set_1.discard(45)
set_1.discard('a')
set_1.discard(10)
print(set_1)
'''

#create single value tuple              tuples program
'''
t_1= ("apple",)
print(t_1)
print(type(t_1))
'''

#relation between id1 and id2
'''
t1 = (1,2,3)
id1 = id(t1)
print(id1)
t2 = (4,5,6)
t1 = t1+t2    #concatenate
id2 = id(t2)
print(id2)
print(*t1,*t2)
'''

#replace the string 'y' to 'Y'
'''
t= (1, 2, 3, 4, ['hai', 'hello', 123], 'python')
str_1 = t[-1].replace('y', 'Y')
t_ = list(t)
t_[-1] = str_1
t = tuple(t_)
print(t)
'''

#replace 2, 3, 4 element into 9, 10, 11
'''
t= (1, 2, 3, 4, ['hai', 'hello', 123], 'python')
t_ = list(t)
t_[1:4] = [9, 10, 11]
t = tuple(t_)
print(t)
'''

#program to add a element into a tuple
'''
t = (10, 20, 30)
print(t)
t1 = t +( 20, )
print(t1)
'''
'''
t = (10, 20, 30)
a = 5
b = t+(a,)
print(b)
'''
#program to remove any 2 element from the tuple
'''
t = (10, 24, 56, 67, 78, 89, 90)
t1 = (t,(list_.remove(56)))
print(t1)
'''

#to get common keys in set
#intersection                                  28/06/24
'''
set_1 = {'a', (4,), 45, 4.4, 3-4j, False, 'a'}
set_2 = {'a', 'b', 'c'}
set_3 = {4.5, 3+4j, 'kiwi', (9,8)}
print(set_1.intersection(set_2))
print(set_2.intersection(set_1,set_3))
'''
'''
set_1 = {'a', (4,), 45, 4.4, 3-4j, False, 'a'}
set_2 = {'a', 'b', 'c', 4.4}
set_3 = {'a', 4.5, 3+4j, 'kiwi', (9,8)}
print(set_1.intersection(set_2))
print(set_2.intersection(set_1,set_3))
'''

#intersection_update
'''
set_1 = {'a', (4,), 45, 4.4, 3-4j, False, 'a'}
set_2 = {'a', 'b', 'c', 4.4}
set_3 = {'a', 4.5, 3+4j, 'kiwi', (9,8)}
print(set_1.intersection(set_2))
print(set_2.intersection(set_1,set_3))
set_1.intersection_update(set_2, set_3)
print(set_1)
set_2.intersection_update(set_1)
print(set_2)
'''

#to get uncommon key in set
#difference
'''
set_1 = {'a', (4,), 45, 4.4, 3-4j, False, 'a'}
set_2 = {'a', 'b', 'c', 4.4}
set_3 = {'a', 4.5, 3+4j, 'kiwi', (9,8)}
print(set_2.difference(set_1))
print(set_3.difference(set_2, set_1))
'''
#difference_update
'''
set_1 = {'a', (4,), 45, 4.4, 3-4j, False, 'a'}
set_2 = {'a', 'b', 'c', 4.4}
set_3 = {'a', 4.5, 3+4j, 'kiwi', (9,8)}
set_3.difference_update(set_1,set_2)
print(set_3)
'''
#symmetric_difference
'''
set_1 = {'a', (4,), 45, 4.4, 3-4j, False, 'a'}
set_2 = {'a', 'b', 'c', 4.4}
set_3 = {4.5, 3+4j, 'kiwi', (9,8)}
print(set_2.symmetric_difference(set_1))
print(set_1.symmetric_difference(set_3))
print(set_3.symmetric_difference(set_2))
'''
#symmetric_difference_update
'''
set_1 = {'a', (4,), 45, 4.4, 3-4j, False, 'a'}
set_2 = {'a', 'b', 'c', 4.4}
set_3 = {4.5, 3+4j, 'kiwi', (9,8)}
set_3.symmetric_difference_update(set_1)
print(set_3)
set_2.symmetric_difference_update(set_3)
print(set_2)
'''
#issubset
'''
s1 = {3, 'a', '$%^', 9.8}
s2 = {3, 'a', 3-4j, '$%^', (45,), 56.4}
print(s1.issubset(s2))


s1 = {3, 'a', '$%^', 9.8}
s2 = {3, 'a', 3-4j, '$%^', 9.8, (45,), 56.4}
print(s1.issubset(s2))
'''
#issuperset
'''
s1 = {3, 'a', '$%^', 9.8}
s2 = {3, 'a', 3-4j, '$%^', (45,), 56.4}
print(s1.issuperset(s2))


s1 = {3, 'a', '$%^', 9.8}
s2 = {3, 'a', 3-4j, '$%^', 9.8, (45,), 56.4}
print(s1.issuperset(s2))
'''
#isdisjoint
'''
s2 = {3, 4, 5, 7}
s3 = {34, 56, 12, 4.5}
print(s2.isdisjoint(s3))
'''

#operators
#'-' difference
'''
s_ = {3, 4, 5.5}
s_1 = {4, 'kiwi', 55}
print(s_-s_1)
'''

#'^' symmetric_difference
'''
s_ = {3, 4, 5.5}
s_1 = {4, 'kiwi', 55}
print(s_^s_1)
'''

#'&'  intersection
'''
s_ = {3, 4, 5.5}
s_1 = {4, 'kiwi', 55}
print(s_&s_1)
'''
#'|" union
'''
s_ = {3, 4, 5.5}
s_1 = {4, 'kiwi', 55}
print(s_|s_1)
'''

#dictionary                                29/06/24
'''
dict_ = {'a':[4, 5, 6], (True, ):{3, 4, 5},
         67: 4.5, False: True, 'a': 45, 'c':[4,5,6]}
print(dict_)
print(type(dict_))
print(len(dict_))
print(dict())
'''

#typecasting


#1. list
'''
print(dict(a=1, b=2.6, c=45))
'''
#2.
'''
print(dict([(34, 'int'), [3.4, [4,5]],
            ['a', 'b'], {34,5}]))
'''
#3.
'''
print(dict(((34, 'int'), [3.4, [4,5]],
            ['a', 'b'], {34,5})))
'''
#4.
'''
print(dict({(34, 'int'), (67, 8), '45'}))

'''

#method in dictionary
#1. indexing
'''
dict_ = {'a':[4, 5, 6], (True, 5):{3, 4, 5},
         67: 4.5, False: True, 'a': 45, 'c':[4,5,6]}
print(dict_['a'])
print(dict_[0])
'''
#'composite key'
'''
print(dict_[(True, 5)])
print(dict_[(1,5)])
print(dict_[True])
'''
#2.get
'''
dict_ = {'a':[4, 5, 6], (True, 5):{3, 4, 5},
         67: 4.5, False: True, 'a': 45, 'c':[4,5,6], (1,5): 'set'}
print(dict_.get(67))
print(dict_.get(1))
print(dict_.get(1, 'no value'))
print(dict_)
'''

# 3. keys                                   1/07/24
'''
d_={'a':'string',34:'int',3.4:'f',(4,5,6):{True,False}}
print(d_.keys())
'''
#4. values
'''
d_={'a':'string',34:'int',3.4:'f',(4,5,6):{True,False}}
print(d_.values())
'''
#5.iteams
'''
d_={'a':'string',34:'int',3.4:'f',(4,5,6):{True,False}}
print(d_.items())
'''

#adding key value pair into a dictionary 
#1.indexing
'''
d_={'a':'string',34:'int',3.4:'f',(4,5,6):{True,False}}
d_[True]=False
d_[(90, 4)]='tuple'
print(d_)
'''

#update
'''
d_={'a':'string',34:'int',3.4:'f',(4,5,6):{True,False}}
d_.update({90: 3.4, 4+4j: 4-34j, 'abc': 'alpha'})
d_.update([[45, 45], (3.4, 'hai'), 'ab', {True, (False, 5)}])
print(d_)
'''



#removing a key value item from a dictionary
#1.popitem
'''
d_={'a':'string',34:'int',3.4:'f',(4,5,6):{True,False}}
d_.popitem()
d_.popitem()
d_.popitem()
print(d_.popitem())
print(d_)
'''
#2.pop
'''
d_={'a':'string',34:'int',3.4:'f',(4,5,6):{True,False}}
d_.pop(3.4)
d_.pop((4,5,6))
print(d_)
'''

#fromkeys
'''
string_= 'string'
print(dict.fromkeys(string_))
print(dict.fromkeys(string_, 'str'))
'''

'''
list_= [3, 4, 5, 6]
print(dict.fromkeys(list_, 'int'))
'''
'''
tup_= ('a',)
print(dict.fromkeys(tup_))
'''
'''
set_= {(90), 'kiwi', 3.4, 56, False}
print(dict.fromkeys(set_, 'key'))
'''

#operators in dictionary
#'*'
'''
d_1 = {3: 45, 4.4: 'float', 5: [5,6,7], '6': 'a'}
d_2 = {0.4: 45, '4.4': 'float', 5.3: [5,6,7], '69':'a'}
print({*d_1, *d_2})
'''

'''
d_1 = {3: 45, 4.4: 'float', 5: [5,6,7], '6': 'a'}
d_2 = {0.4: 45, '4.4': 'float', 5.3: [5,6,7], '69':'a'}
print(d_1|d_2)
'''


#program to increment the value of 'b'
'''
p_ ={'a':1, 'b':2, 'c':4}
print(p_['b'])
p_['b'] = p_['b']+4
print(p_)
'''

#difference between pop and popitems
'''
d_ = {3: 45, 4.4: 'float', 5: [5,6,7], '6': 'a'}
d_.popitem()
d_.popitem()
print(d_.popitem())
print(d_)
'''
'''
d_ = {3: 45, 4.4: 'float', 5: [5,6,7], '6': 'a'}
d_.pop(3)
print(d_)
'''

#create a dictionary with'0' as the value for all the key
'''
l=['a', 'b', 'c', 'e']
d_= {key : 0 for key  in l}
print(d_)
'''

#merge two dictionary
'''
dict1 = {'a':(4,5), 'b':35, 'c':50}
dict2 = {3: 45, 4.4: 'float', 5: [5,6,7], '6': 'a'}
merged_dict = (dict1|dict2)
print(merged_dict)
'''


#difference between pop remove and discard
#pop      remove an element from the set
'''
set_1 = {'a', (4,), 45, 4.4, 3-4j, 67, 'a'}
set_1.pop()
print(set_1.pop())
print(set_1)
'''

#remove              remove the specific elements
'''
set_1 = {'a', (4,), 45, 4.4, 3-4j, False, 'a', 23}
set_1.remove((4,))
print(set_1)
'''

#discard            remove the specific item
'''
set_1 = {'a', (4,), 45, 4.4, 3-4j, False, 'a', 23}
set_1.discard(45)
set_1.discard('a')
set_1.discard(10)
print(set_1)
'''

#difference between difference and symmetric difference

#difference(-)
'''
s_ = {3, 4, 5.5}
s_1 = {4, 'kiwi', 55}
print(s_1-s_)
print(s_-s_1)
'''


#symmetric difference(^)
'''
s_ = {3, 4, 5.5}
s_1 = {4, 'kiwi', 55}
print(s_^s_1)
'''

#what is the output
'''
a = {'apple', 'orange', 'grapes'}
a_= a.add({'kiwi'})
print(a)
'''

#output
#a[1]
'''
a = {'apple', 'orange', 'grapes'}
print(a[1])     #unhasable error
'''
'''
s = {1, 2, 3, 4, 5, 6}
print(s.add([10,20]))
print(s.add((25,40)))         #unhasable error
'''



#operators in python                               2/07/24
#1.Arithmetic operator
'+,-,*,/,//,%,**'

#2. Relational operator
'<,>,<=,>=,=,==,!= --> output is in boolean type'
'''
print(3<4, 4>3)
print(3<=4, 4<=4, 5<0.1)
print(3>=4, 4>=4, 5>0.1)
print('hai'=='hai', 'hai'=='hi')
print('hai'!='hai', 'hai'!='hi')
print(3>4,5>0.1)
print('hai'!='hai', 'hai'!='bye')
'''

#3. Logical operators
'or, and, not'
#or    -->this operator returns true if one contion will be correct
'''
print(45<45 or 45>=45)
print(20>30 or 30<50)
'''
#and   -->this return true if both statement or condition is true
'''
print(1<5 and 6<4)
print(4>1 and 3>2)
'''
 #not  -->reverse the result, returns false if the result is true
'''
print(not(5>3 and 5<10))
print(not(5>3 and 5>2))
'''

#4. bitwise operators
#1. or--> '|'   covert the number to binary then perform the or operation
'''
n1=34
n2=40
print(n1|n2)
n3=5
print(n1|n2|n3)
'''

#2. and--> '&'
'''
n1=34
n2=40
print(n1&n2)
n3=62
print(n1&n2&n3)
'''

#3. not-->'~'
'''
print(~34)
print(~-40)
'''

#4. xor-->'^'
#same number--->0 and different number--->1
'''
n1=45
n2=40
print(n1^n2)
n3=20
n5=20
print(n3^n5)
'''

#5. assignment operators
#=
'''
n=89
print(n)
'''
#+=
'''
n=n+1
n+=10
print(n)
'''
#*=
'''
n="hi"
n*=4
print(n)
'''
#/=
'''
n=9
n/=3
print(n)
'''
#%=
'''
n=34
n%=2
print(n)
'''
#-=
'''
n=34
n-=2
print(n)
'''

#**=
'''
n=34
n**=8
print(n)
'''

#//=
'''
n=8
n//=2
print(n)
'''

#6.identity operator
#'is' --> to check the address is same
'''
print(10==10)
n=20
n1=20
print(n is n1)
'''

#'is not'--> to check the address is different
'''
n2=45
n3='hey'
print(n2 is not n3)
'''

#7.membership operator
#'in'
'''
print('h' in 'hai', 'H' in 'hai')
print('h'=='hai')
print('bye' in ['hai','hello','bye',])
print('bye' in {'hai':3, 'hello':45, 'bye':4.5})
'''

#not in
'''
print('bye' not in {'hai':3, 'hello':45, 'bye':4.5})
print('45' not in {'hai':3, 'hello':45, 'bye':4.5})
print('hii' not in {'hai':3, 'hello':45, 'bye':4.5})
'''

#


































































