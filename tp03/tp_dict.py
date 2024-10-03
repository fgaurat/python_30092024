

d = {
    "name":"GAURAT",
    "firstName":"Fred",
    "jobs":[
        "dev",
        "formateur",
    ]
}

print(d['name'])
d['age'] = 48

print(d)


l1 = ['key1','key2','key3','key4']
l2 = ['value1','value2','value3']
l3 = list(zip(l1,l2))
print(l3)
d = dict(l3)
print(d)