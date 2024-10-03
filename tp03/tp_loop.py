
l =[10,20,30,40,50]


for i,d in enumerate(l):
    print("pos",i,"data",d)

print(50,'-')
the_data = {
    "name":"GAURAT",
    "firstName":"Fred",
    "age":48,
    "job":"dev"
}

for k,v in the_data.items():
    print(k,v)


keys = the_data.keys()
values = the_data.values()
print(keys)

if "fname" in keys:
    print("ok")
else: 
    print("ko")