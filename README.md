# first-py-codes
print("hello world")\
def new_func():
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


    my_num = "do it"    # snake case as each word is seperated by underscore
    _my_num = 'do it'
    myNUM = 'do it'     # camel case when first letter is small and rest are capital
    MYnum = 'do it'     
    my_num2 = 'do it'
    MyNum = 'do it'     # pascal case when each word start with capital letter
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
    print(x*y-z)



    a,s,d,f,g,h,j,k,l, = 2,4,3,6,7,8,4,1,4


    print(a+s+d-f/g*+h-j-k-l)
