
# def add(l:List):
def add(*l):
    print(l)
    r= 0
    for i in l:
        # r=r+i
        r+=i
    return r 


# l =[10,20,30,40,50]
# r = add(*l) #add(10,20,30,40,50)
# print(r) # 150

r = add(10,20,30,40)
print(r) # 150


# print("Bonjour "+str(48))
# age = 48
# print("Bonjour",age)



a,b,*c= [1,2,3,4,5,6,7,8]
print(a,b)
print(c)

# a,b,*d = [*c]

print(50*'-')
l =[10,20,30,40,50]
# print(l[0],l[1],l[2]...)
print(*l)



def hello(**kwargs):
    print(kwargs['name'])


hello(name="Gaurat",firstName="Fred",job="Dev",age=48)

print(50*'-')

conf_print={
    "sep":"-",
    "end":"toto"
}

l =[10,20,30,40,50]
print(*l,**conf_print)