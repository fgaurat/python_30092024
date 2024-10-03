def fib(n):    # write Fibonacci series up to n
    """
    Print a Fibonacci series up to n.
    """ #docstring
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        # print(a)
        a, b = b, a+b
    print()

def fib2(n=30):    # return Fibonacci series up to n
    """
    return Fibonacci series up to n.
    """ #docstring
    l=[]
    a, b = 0, 1
    while a < n:
        l.append(a)
        a, b = b, a+b
    return l

# Now call the function we just defined:
fib(2000)

r = fib2(2000)
print(r) # [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597 ]

r = fib2()
print(r)

print(50*'-')



def the_function(n=""):
    global v # c'est mal
    print(v)
    v = "Toto"
    if True:
        i=12
    print(i)


v = "the value"


print(v)
the_function()
print(v)

def f(a, L=[]):
    L.append(a)
    return L
f(1)

print(50*'-')

def hello(name,firstname,age):
    print("Bonjour "+name+" "+firstname+" "+str(age))


hello("GAURAT","Fred",48)
hello(firstname="Fred",name="GAURAT",age=48)
hello("GAURAT","Fred",age=48)
hello("GAURAT",firstname="Fred",age=48)