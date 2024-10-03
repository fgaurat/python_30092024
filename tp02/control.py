# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')


l = ["Value 1","Value 2","Value 3","Value 4"]
print(l)

for the_value in l:
    print(the_value)

for i in range(10):
    print(i)


for posit in range(len(l)):
    print(str(posit)+" "+l[posit])

r = range(3)    
r1 = list(range(3))
print(r) # [0,1,2]


print(50*'-')
l=[10,50,36,53,435,8,54]
to_find = 533333


for the_value in l:
    print(the_value)
    if to_find == the_value:
        print("ok")
        break
else:
    print('pas trouvé')



a = True
if a:
    # todo: faire un truc
    pass