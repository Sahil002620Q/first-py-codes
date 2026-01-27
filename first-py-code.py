# first-py-codes
x = 4
y = "hello zorin"
print(x)
print(y)

#comment , to start comment just use hashtage


# x will be '3'  
# y will be 3
# z will be 3.0
x = int(4)
y = float(4)
z = str(4) 
print(x)
print(y)
print(z)


x = 6
y = "YUP" 
z = 9.99        
print(type(x))
print(type(y))
print(type(z))



""" we can use " something "  or 'something' means we can
use either single or double inverted commas"""
x = "need concictency"
print(x)
x = 'need concictency'
print(x)


a = 2
A = 'you can do it'
print(a)
print(A)



"""
   A variable name must start with a letter or the underscore character
   A variable name cannot start with a number
   A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ) 
   Variable names are case-sensitive (age, Age and AGE are three different variables)
   A variable name cannot be any of the Python keywords.
"""


my_num = "do it x1"    # snake case as each word is seperated by underscore
_my_num = 'do it x2'
myNUM = 'do it x3'     # camel case when first letter is small and rest are capital
MYnum = 'do it x4'     
my_num2 = 'do it x5'
MyNum = 'do it x6'     # pascal case when each word start with capital letter
print(my_num)
print(_my_num)
print(myNUM)     
print(MYnum)
print(my_num2)
print(MyNum)


"""
   2mynum = "do it"
   my-num = "do it"
   my num = "do it"
 This example will produce an error in the result  """

#printing multiple values
x,y,z = 'one','two','three'
print(x)
print(y)
print(z)


x = y = z = 'new'
print(x)
print(y)
print(z)

fruit = ['apple',"mango",'grapes']
x,y,z = fruit
print(x)
print(y)
print(z)



#print multiple variable using single print()

x,y,z = 'hello','myself','sahil'
print(x,y,z)



x,y,z = 10,20,30
print(x+y+z)

x,y,z = 'python ','is ','awesome '    # need to give space before closing inverted comma
print(x+y+z)
#Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
# you can add num by num or word by word but you can not add word and num it will throw an error

x,y = 'number',2
print(x,y)


x = "yup"
def myfunc():
    print("are you fine ?  " + x)
myfunc()



#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
x = 4
def myfunc():
    x = 3
    print("three" + x)
    myfunc()
    print("four" + x)


x = 'f '
def myfunc():
    x = "hell"
    print("go to " + x)

myfunc()

print("what the " + x)





def myfunc():
    global x 
    x = 'text'
myfunc()
print("new " + x)    #here i gave space so that after new there will be space and it doesn't look like newtext


x = 'i am useless'
def myfunc():
    global x
    x = 'i know'
myfunc()
print(x)


"""
Text Type:   	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:   	NoneType
"""

print("------------------")

x = 1 
print(x)
print(type(x))


x = 1.1
print(x)
print(type(x))


x = 1j
print(x)
print(type(x))

x = 'hello'
print(x)
print(type(x))

x = ['hello','hi','wasup']
print(x)
print(type(x))

x = ('hello','hi','wasup')
print(x)
print(type(x))

x = True
print(x)
print(type(x))

x = bytearray(7)
print(x)
print(type(x))

x = b'hello'
print(x)
print(type(x))

x = {'hello','hi'}
print(x)
print(type(x))

x = None
print(x)
print(type(x))

x = {'hello' : 'new', 'hi' : 'old'}
print(x)
print(type(x))

x = frozenset({'hello','hi'})
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))

x = range(7)
print(x)
print(type(x))



x =  int(5)     
print(x)    
print(type(x))

x =   str('hello')    
print(x)
print(type(x))

x =    float(9.9)   
print(x)
print(type(x))

x = bool(8)    
print(x)
print(type(x))

x = bytes(7)   
print(x)
print(type(x))

x = b'hello' 
print(x)
print(type(x))

x =  complex(1j)  
print(x)
print(type(x))

x =  dict( name = 'sahil',age = 7)   
print(x)
print(type(x))

x =  set(('hello','name'))   
print(x)
print(type(x))

x =  tuple(('name','age'))     
print(x)
print(type(x))

x =  list(('age','date'))
print(x)
print(type(x))

x =  bytearray(7)  
print(x)
print(type(x))

x =   frozenset(('hell',"heaven"))    
print(x)
print(type(x))

x =   memoryview(bytes(5))    
print(x)
print(type(x))


x = 2
y = 36934855785757758657
z = -85


print(type(x))
print(type(y))
print(type(z))

x = 1.547
y = 1.0
z = -8.87

print(type(x))
print(type(y))
print(type(z))


x = 45e5
y = 65E7
z = -9.9e93


print(type(x))
print(type(x))
print(type(x))


x = 7+8j
y = 9j
z = -8j


print(type(x))
print(type(x))
print(type(x))

x = 3
y = 5.3
z = 98j


a = int(x)
b = float(y)
c = complex(z)

print(type(a))
print(type(b))
print(type(c))


#intresting

import random
print(random.randrange(1,20))



x = 4
y = 4j

x = float(x)
y = float(x)


print(x)
print(x)

x = 4.4
y = 4j

print(x)
print(y)

x = float(3)
y = float(3.3)
z = float("3")
e = float("7.8")

print(x)
print(y)
print(z)
print(e)


x = int(3)
y = int(4.4)
z = int("3")
#e = int("9.9") not possible

print(x)
print(y)
print(z)
#print(e)  not possible 


x = str("s5")     # inverted commas are compulsory
y = str(7)
z = str(9.9)

print(x)
print(y)
print(z)


#using quotes inside string

print("he said yup bro!")
print('he said "yup bro!" ')
print("he said 'yup bro!' ")


x = "hello"
print(x)

x = """i know what's happening but i also  know
nothing is in my control"""

print(x)

a = "hello"
print(a[2])

print('just for space')

for x in 'something':
 print(x)

print('string length')   # string length

x = 'hello world' 
print(len(x))

#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "hi my name is sahil and currently i'm doing code practice in python"
print("sahil" in txt)
print("hello" in txt )



 
