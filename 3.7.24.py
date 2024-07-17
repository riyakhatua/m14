#decision making
#types of decision making
#if condition
'''
if True:
    print('hai')

if False:
    print('hai')
    '''


#---
'''
if bool(1):
    print('bye')
if bool(0):
    print('bye')
    '''

#1.
'''
if bool(0) or bool(1):
    print('bye')
    '''
#2.
'''
if bool(0) and bool(1):
    print('bye')
    '''


'''
n=input("enter:")
if n:
    print('data is present')
    print('data is not present')
    '''
#2.if-else condition
'''
n=input("enter:")
if n:
    print('data is present')
else:
    print('data is not present')
    '''
#3. nested if-else condition
'''
if True:
    print('main if')
    if False:
        print('nested if')
    else:
        print('nested else')
else:
    print('main else')
    '''
#4.elif condition
'''
if True:
    print('A')
elif True:
    print('B')
elif True:
    print('c')
else:
    print(False)
    '''

'''
if True:
    print('A')
elif False:
    print('B')
elif False:
    print('c')
else:
    print(False)
'''
'''
if False:
    print('A')
elif False:
    print('B')
elif False:
    print('c')
else:
    print(False)
    '''
#1. program to check the given number is even or odd
'''
num_=int(input("enter a number:"))
condition_=num_%2==0
if condition_:
    print('even number')
else:
    print('odd number')
    '''
#2. program to check whether it is vowel or not
'''
char_=input()
vowel='aeiouAEIOU'
if char_ in vowel:
    print('vowel')
else:
    print('not a vowel')
    '''
#3. program to check whether the string is pallindrom or not
'''
string=input("enter string:")
if (string==string[::-1]):
   print('is a pallindrom')
else:
    print('not a pallindrom')
    '''

'''
string=input("enter string:")
condition_=(string[::-1])
if condition_:
   print('is a pallindrom')
else:
    print('not a pallindrom')
    '''




#4. program to check whether the number is pallindrom or not
'''
num_=input("enter the number:")
if(num_==num_[::-1]):
    print("is a pallindrom")
else:
    print("not a pallindrom")
    '''

'''
num_=input("enter the number:")
condition_=(num_[::-1])
if condition_:
    print("is a pallindrom")
else:
    print("not a pallindrom")
    '''

#5. program to check whether a year is leap year or not
'''
num_=int(input("enter a number:"))
condition_=num_%4==0
if condition_:
         print('is a leap year')
else:
         print('not a leap year')
       '''
#                                             4/7/24
#6.program to check whether the number is perfect square root or not
'''
i = int(input("Enter:"))
s = i **0.5
if s * s ==i:
    print('is a perfect square')
else:
    print('not a perfect square')
    '''

#7.program to check if the given character is alphabet or number or a
#special character
'''
char_ = input("Enter the string:")
if char_.isalpha():
    print("alphabet")
elif char_.isnumeric():
    print("number")
elif not char_.isalnum():
    print("a special character")
'''

#for 1 character only
'''
char_ = input("Enter the string:")
if  len(char_) == 1 and char_.isalpha():
    print("alphabet")
elif len(char_) == 1 and char_.isnumeric():
    print("number")
elif len(char_) == 1 and not char_.isalnum():
    print("a special character")
    '''

#8.print pass if mark is greater than 35 else fail and mark is greater
#than 60 print first class
'''
mark = int(input("enter the marks:"))
if 35 <= mark <60:
    print("pass")
elif mark  >60:
    print("first class")
else :
    print(" fail")
'''
#9.check the starting character is vowel or not
'''
s_ = input("Enter the string:")
start_char = s_[0]
if start_char in'aeiouAEIOU':
    print('vowel')
else:
    print('not vowel')
    '''

#10.program to check if the given list has even legth or odd
'''
elements = input("enter the elements : ").split()
if len(elements)%2 == 0:
    print('even length')
else:
    print('odd length')
    '''
#11.check the number of keys in the dictionary if the number is even
#print as it is otherwise add a new key to make it even and print it
'''
d = {}
d.update({4:5, 'a':4, 'b':34})
if len(d)% 2 == 0:
    print(d)
else:
    key = input("enter a key :")
    value = input("enter a value:")
    d[key] = value
    print(d)
    '''
#program to check largest number in user input
'''
n1= int(input("Enter"))
n2= int(input("Enter"))
n3= int(input("Enter"))
if n1>=n2 and n1>=n3:
    print(n1,  'is greater')
elif n2>=n1 and n2>=n3:
    print(n2, 'is greater')
else:
    print(n3, 'is greater')
    '''
#program to check the smallest number in user input
'''
n1= int(input("Enter"))
n2= int(input("Enter"))
n3= int(input("Enter"))
if n1<n2 and n1<n3:
    print(n1,  'is smaller')
elif n2<n1 and n2<n3:
    print(n2, 'is smaller')
else:
    print(n3, 'is smaller')
    '''
#program for random value
#1.randint
'''
import random
print(random.randint(10, 20))
'''
#
'''
import random
l_= [4,4.5, 12, 67]
index_= random.randint(0, len(l_)-1)
print(l_[index_], "at the index", index_)
'''

#2. choice
'''
import random
places = ['goa', 'varkala', 'karnataka', 22, 2.5]
print("let's visit", random.choice(places), ":)")
'''

#program to get tail or head
'''
import random
num_=random.randint(0,1)
if num_==0:
    print('head')
else:
    print('tail')
    '''

#program to guess a number
'''
import random
name = input("what is your name")
print("hey", name, "let's start the game")
user_guess= int(input("guess a number:1 to 10"))
computer_guess=random.choice((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(computer_guess)
if user_guess==computer_guess:
    print("you win")
elif user_guess<computer_guess:
    print('guess larger number')
elif user_guess>computer_guess:
    print('guess lower number')
else:
    print('guess only numbers in the tuple')
 '''

#scissor, stone, paper
'''
import random
name = input("what is your name :")
print("hey", name, "let's start the game")
computer_items = random.choice(['scissor', 'rock', 'paper'])
user_input = input("scissor or rock or paper:")

if computer_items == user_input:
    print('draw')
elif computer_items == 'scissor':
    if user_input == 'rock':
        print('you won rock hits scissor')
    else:
        print('you lost scissor cuts the paper')
elif computer_items =='rock':
    if user_input == 'paper':
        print(user_input,'won paper wrap the rock')
    else:
        print(user_input,'lost rock hits the scissor')
        '''

#Looping                                          #06/07/24
#1.While loop
#program to print a number from 1 to 5
'''
i = 1
while i<=5:
    print(i)
    i = i+1
    '''
#program to print a number from 5 to 1
'''
i = 5
while i>=1:
    print(i)
    i = i-1
    '''
#
'''
i = 5
while i>=1:
    print(i)
    i -= 1
    '''
#write a program to print 'bangalore' 10 times
'''
j = 1
while j <= 10:
    print('bangalore', j)
    j+=1
    '''
#write program to print your name n times
'''
name_ = input("enter your name:")
n = int(input("give the count:"))
i = 1
while i <= n:
    print(name_, i)
    i += 1
'''


#program to square the number from start to end
'''
a_ = int(input("enter the start number:"))
b_ = int(input("enter the end number:"))
while a_ <= b_:
    print(a_**2)
    a_ +=1
    '''

#with method--> append
'''
a_ = int(input("enter the start number:"))
b_ = int(input("enter the end number:"))
l_ = []
while a_ <= b_:
    l_.append(a_**2)
    a_ += 1
print(l_)
'''

#without method
'''
a_ = int(input("enter the start number:"))
b_ = int(input("enter the end number:"))
l_ = []
while a_ <= b_:
    l_ = l_+[a_**2]
    a_ += 1
print(l_)
'''
    
#program to get the character and its indexes
'''
str_ = input("enter the string:")
index_= 0
while index_ <= len(str_)-1:
    print(index_, str_[index_])
    index_ += 1
    '''
#pack as tuple in list
'''
str_ = input("enter a string:")
index_ = 0
list_ = []
while index_< len(str_):
    list_.append((index_, str_[index_]))
    index_ += 1
print(list_)
'''

#program to print nested list with character and its ascii value
'''
str_ = input("enter  the string:")
i = 0
while i< len(str_):
    print(str_[i], ord(str_[i]))
    i = i+1
'''
#with list
'''
str_ = input("enter  the string:")
i = 0
l_ = []
while i< len(str_):
    l_ +=[[str_[i], ord(str_[i])]]
    i = i+1
print(l_)
'''

#program to get elements and its length by taking the input from user
'''
str_=input("enter the string:").split()
print(len(str_))
index_ =0
while index_<= len(str_) -1:
    print(index_, str_[index_])
    index_ = index_ +1
    '''
    

#program to check if the given datatype is of string datatype


#program to check a data is float datatype
#program to convert lowercase to uppercase
'''
inp_ = input("enter:")
str_ = ''
index = 0
while index <len(inp_):
    str_ += inp_[index].upper()
    index += 1
print( str_)
'''
#program to covert uppercase to lowercase
'''
inp_ = input("enter:")
str_=''
index = 0
while index<len (inp_):
    str_ += inp_[index].lower()
    index += 1
print(str_)
'''
#program to covert uppercase to lowercase and lowercase to uppercase
#with method
'''
inp_ = input("enter:")
if inp_.islower():
    print(inp_.upper())
else:
    print(inp_.lower())
    '''


#program to get the number ending with even number
'''
numbers = [2,3,4,45,43,89,12,90,77,65,34,234,89,45,620]
i = 0
while i<=len(numbers):
    if int(str(numbers[i])[0]) % 2 == 0:
        print(numbers[i])
    i +=1
    '''
# covert uppercase to lowercase
'''
inp_ = input("enter:")
if inp_.islower():
    print(inp_.upper())
else:
    print(inp_.lower())
    '''
#program to convert lowercase to uppercase without method
#'ord' and 'chr'
'''
inp_= input("enter:")
if 'a' <= inp_ <= 'z':
    print(ord(inp_))
    print(ord(inp_) - 32)
    print(chr(ord(inp_)-32))
    '''

#program to convert uppercase to lowercase and lowercase to uppercase
#without method (one character)
'''
inp_= input("enter:")
if 'a' <= inp_ <= 'z':
    print(chr(ord(inp_)-32))
elif 'A' <= inp_ <='z':
    print(chr(ord(inp_) +32))
    '''
#program to convert uppercase to lowercase and lowercase to uppercase
#without method
'''
string_ = input("enter:")
index_=0
new_str =''
while index_< len(string_):
    if 'a' <= string_[index_]<= 'z':
        new_str += chr(ord(string_[index_])-32)
    elif 'A' <= string_[index_] <= 'Z':
        new_str += chr(ord(string_[index_])+32)
    else:
        new_str += string_[index_]
    index_ +=1
print(new_str)
'''
#program to get the string in reverse order
'''
inp_ = input("enter a string:")
print(inp_[::-1])
'''

'''
inp_ = input("enter a string:")
i = 0
n_s = ''
while i < len(inp_):
    n_s = inp_[i] +n_s
    i += 1
print(n_s)
'''
#program to get the length of string in a list
'''
names = ['eve','james','bill','steve','mill','amul']
len_ = []
index = 0
while index<len(names):
    len_.append(len(names[index]))
    index +=1
print(len_)
'''
#
#create a dictionary with starting character and word in the list
'''
names = ['eve', 'james', 'bill', 'steve', 'mill', 'amul']
dic_ ={}
i = 0
while i< len(names):
    dic_[names[i][0]] = names[i]
    i += 1
print(dic_)
'''


#create a dictionary with word and length word in the list
'''
names = ['eve', 'james', 'bill', 'steve', 'mill', 'amul']
dic_ = {}
i = 0
while len(names) > i:
    dic_[names[i]] = len(names[i])
    i += 1
print(dic_)
'''

#program to get a number which is even
'''
num_=[2,3,4,45,43,89,12,90,77,65]
while num_%2!=0:
    print("num_")
    '''





   
#program to get factorial of a number
'''
num_ = int(input("enter a num:"))
i = 1
fact_ = 1
while num_ >=i:
    fact_ = fact_ *i
    i += 1
print(f"factorial of", num_, 'is', fact_)
'''

#program to get 1 to user input
'''
input_ = int(input("enter :"))
i = 1
while i<= input_:
    print(i)
    i += 1
    '''


#program to get 1 to 10
'''
i = 1
while i<=10:
    print(i)
    i = i+1
    '''
#program to get -1 to -10
'''
i = -1
while i>=-10:
    print(i)
    i = i-1
    '''
#program to get 10 to 1
'''
i = 10
while i>= 1:
    print(i)
    i -= 1
    '''
#program to get 1 to user input
'''
input_ = int(input("enter :"))
i = 1
while i<= input_:
    print(i)
    i += 1
    '''
    

#program to get -20 to -10
'''
i = -20
while i<= -10:
    print(i)
    i += 1
    '''
#program to get 1 to -10
'''
i = 1
while i>= -10:
    print(i)
    i -= 1
    '''
#program to get -1 to 20
'''
i = -1
while i<= 20:
    print(i)
    i += 1
    '''
#program to get -10 to -1
'''
i = -10
while i<= -1:
    print(i)
    i +=1
    '''

#building a dictionary of word and length pair
'''
s_ = "This is a bunch of words"
words_= s_.split()
print(words_)
w_= dict()
i = 0
while i <len(words_):
    w_[words_[i]] = len(words_[i])
    i += 1
print(w_)
'''

#flipping keys and values of the dictionary
'''
dic = {'a':1, 'b':4, 'c':8}
items_ = dic.items()
items_list = list(items_)
print(items_list)
d_={}
i = 0
while i < len(items_list):
    d_[items_list[i][1]] = items_list[i][0]
    i += 1
print(d_)
'''


#program to count the number of each character in a string
'''
str1 = "guido vann Rossum"
d_ = dict()
i = 0
while i<len(str1):
    d_[str1[i]] = str1.count(str1[i])
    i += 1
print(d_)
'''
    
#program to create a dictionary with word and it's count
'''
senten_ = "hello world welcome to python hello hi world welcome to java"
words_ = senten_.split()
d_ = dict()
i = 0
while i<len(words_):
    d_[words_[i]] = len(words_[i])
    i += 1
print(d_)
'''
#dictionary of character and askii value pair
'''
s = "absABS"
'''
#building a dictionary whose price value is more than 200
'''
prices = {"AEMC":24.45,
          "APAL":612.45,
          "JBN":200.45,
          "HP":37.80,
          "FB":10.75}
price_tuple = tuple(prices.items())
i = 0
d_price = {}
while i < len(price_tuple):
    if price_tuple[i][1] > 200:
        d_price[price_tuple[i][0]] = price_tuple[i][1]
    i += 1
print(d_price)
'''
#program to get all the alphabet from the string
'''
str_ = input("enter:")
alphabets = ''
i = 0
while i < len(str_):
    char = str_[i]
    if char.isalpha():
        alphabets += char
        i += 1
        '''

#program to get all the speical characters in a string
'''
str_= input("enter:")
char_= []
i=0
while i<len(str_):
    char=str[i]
    char_.append(char)
    i += 1
    '''

    
        
#program to only integer from the list
'''
data = ["hii", "hello", "12.3", 12, 19, 6.2]
i =0
while i<len(data):
    if type(data[i]) == int:
        print(data[i])
    i += 1
    '''

#with method
'''
data = ["hii", "hello", "12.3", 12, 19, 6.2]
i =0
while i<len(data):
    if isinstance(data[i], int):
        print(data[i])
    i += 1
    '''
    
#program to print only vowel from the string         end = ''
'''
s_= "python selenium"
vowel = "aeiou"
i = 0
while i <len(s_):
    if s_[i] in vowel:
        print(s_[i])
    i += 1
    '''
#program to get only alpha numeric character from a string
'''
s_ =input("enter a string:")
str_= ''
i = 0
while i<len(s_):
    if s_[i].isalnum():
        str_ = str_+ s_[i]
    i += 1
print("str_")
'''

    
#WAP to check if the given list of string which is pallindrom
'''
element = input("enter the string:").split()
i = 0
l_ = []
while i<len(element):
    if element[i] == element[i][::-1]:
        l_ += [element[i]]
    i += 1
print(l_)
'''
    

#replace all the vowel with star(*) in the string "hello world"
'''
str_= "hello world"
i = 0
ne_= ''
while i<len(str_):
    if str_[i] in 'aeiou':
        ne_ = ne_ + '*'
    else:
        ne_ = ne_+ str_[i]
    i += 1
print(ne_)
'''
#with method
'''
str_= "hello world"
i = 0
ne_= ''
while i<len(str_):
    if str_[i] in 'aeiou':
        ne_ += str_[i].replace(str_[i],"*")
    else:
        ne_ += str_[i].replace(str_[i],str_[i])
    i += 1
print(ne_)
'''





#for loop                                    #15/07/24
#program to iterate ant iterable
'''
str_ = 'python'
for i in str_:
    print(i)
    '''

'''
list_ = ['python','java','perl','css',45,2.4]
for i in list_:
    print(i)
    '''

#for dictionary                                16/07/24
'''
dict_ = {
    'python':56,
    'java':56.5,
    'pearl':45,
    'css':True,
    2.4:[4,5,]}
'''


#control statement
#1. break
#program to break when the number is 5
'''
i = 1
while i < 10:
    if i == 5:
        break
    else:
        print(i)
    i +=1

'''


#2. continue
#program to skip all the even number
'''
t_ = (34, 5, 3, 68, 4, 90, 77, 23)
for num in t_:
    if num % 2 == 0:
        continue
    print(num)
    '''


#3. pass
'''
for i in [4, 5, 6]:
    pass
for i in 'hai':
    print(i)
    '''

#inbuilt-functions
#1. range
the range function generate a sequence of numbers
#2. enumerate
#3. zip/ zip_longest







































































































