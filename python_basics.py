#print statement
print("hello world")
print(233)
print(4.9)
print("welcome to")
print("the world of python")
print("\"welcome to the world of python\"")
a=6.9
print(type(a))
print("python\n"*3)
forename = input("enter your name")
print("hello ",forename)

#OUTPUT
'''
hello world
233
4.9
welcome to
the world of python
"welcome to the world of python"
welcome to the world of python!"welcome to the world of python"
enter the number5
<class 'int'>
<class 'float'>
python
python
python
enter your nameaiswarya
hello  aiswarya

'''

num = int(input("enter the number"))
print(type(num)) #to get variable type


a=6.9
print(type(a))

#INDEX VALUE
s="python"
print(s[0:4])
print(s[:3])
print(s[0:6:2])
print(s[-5:-2])
print(s[::-1])

fruits =['apple','orange','grapes','banana']
print(fruits[2])
print(fruits[:2])
fruits.append(9)
print(fruits[:])
print(fruits.count(9))

#OUTPUT
'''
pyth
pyt
pto
yth
nohtyp

grapes
['apple', 'orange']
['apple', 'orange', 'grapes', 'banana', 9]
1

'''

#STRING FUNCTIONS

s="pyThOn"
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.swapcase())

#OUTPUT
'''
python
PYTHON
Python
PYtHoN'''

key=(23,56,"pin")
key[2]

#output
"""pin"""


d1={'hari':34,"maya":33,"john":44}
d1.items()
d1.get("john")
d1.keys()
d1.values()

#output

'''dict_items([('hari', 34), ('maya', 33), ('john', 44)])
44
dict_keys(['hari', 'maya', 'john'])
dict_values([34, 33, 44])'''

#tuple

s={2,6,3,8,4,1,6,4,3,5,2}
print(s)

#output ---{1, 2, 3, 4, 5, 6, 8}

#positive or negative

num = int (input("enter  number : "))
if(num>0):
  print("positive")
elif(num<0):
  print("negative")
else:
  print("it's zero")

#output
'''enter  number : 7
positive'''




#delivery charge

charge = float(input(" enter the food charge  "))
if(charge>1000):
  print("free delivery,,PAYABLE= ",charge)
elif(charge<1000 and charge>500):
    print("total charge = ",charge+50)
else:
  print("total charge = ",charge+100)

#output
'''enter the food charge  6888
free delivery,,PAYABLE=  6888.0
'''



#for loop

fruits =['apple','orange','grapes','banana']
for i in fruits:
  print("i like "+i)
#output
'''
i like apple
i like orange
i like grapes
i like banana
'''
#count

medals = ["gold","silver","gold","bronze","gold","silver"]
gold=silver=bronze=0
for i in medals:
  
  if(i=="gold"):
    gold+=1
  elif(i=="silver"):
    silver+=1
  else:
    bronze+=1
print("gold : ",gold,"silver : ",silver,"bronze : ",bronze)
#output
"""gold :  3 silver :  2 bronze :  1"""


#fizzbuzz

for i in range(1,101):
    if(i%3==0 and i%5==0):
      print("FizzBuzz")
    elif(i%5==0):
      print("BUZZ")
    elif(i%3==0):
      print("Fizz")
    else:
      print(i)
#output
"""1
2
Fizz
4
BUZZ
Fizz
7
8
Fizz
BUZZ
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
BUZZ
Fizz
22
23
Fizz
BUZZ
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
BUZZ
Fizz
37
38
Fizz
BUZZ
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
BUZZ
Fizz
52
53
Fizz
BUZZ
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
BUZZ
Fizz
67
68
Fizz
BUZZ
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
BUZZ
Fizz
82
83
Fizz
BUZZ
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
BUZZ
Fizz
97
98
Fizz
BUZZ"""

#even and odd

numbers=[1,2,3,4,5,6,7,8,9]
odd=[]
even=[]
while len(numbers)>0:
  number=numbers.pop()
  if(number%2==0):
    even.append(number)
  else:
    odd.append(number)

print("even list : ",even)
print("odd list",odd)
#output
'''even list :  [8, 6, 4, 2]
odd list [9, 7, 5, 3, 1]'''

#password guesser

password ="1234"
guess=input("enter your guess(HINT : password is a 4 digit no)")
while(password!=guess):
  print("try again")
  guess=input("enter your guess(HINT : password is a 4 digit no)")
print("success")
#output
'''enter your guess(HINT : password is a 4 digit no)3456
try again
enter your guess(HINT : password is a 4 digit no)1234
success'''


#number guesser

import random
secret= random.randint(1,10)
while(True):
  guess=int(input("enter your guess between 1-10\t"))
  if(secret>guess):
   print("think higherr")
  elif(secret < guess):
    print("think  lower")
  else:
     print("\n\tcongratsss!!")
     break
#output

'''enter your guess between 1-10	7
higherr
enter your guess between 1-10	9

	congratsss!!'''
  
#function

def cube(n):
      return(n**3)
cube(5)     #output-- 125