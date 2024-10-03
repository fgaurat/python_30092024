import sys
print("Hello World")

# HelloWorld => UpperCamelCase, PascalCase, CapsWord
# helloWorld => camelCase
# hello_world => snake_case
# hello-world => kebab-case
the_world_is_flat = True  # inférence de type
if the_world_is_flat:
    print("Be careful not to fall off!")
    print("truc")


s = "Bonjour\nil fait beau"
print(s)
p="c:\\newproject\\truc"
p = r"c:\newproject\truc"
print(p)
s = "L'orage gronde"
print(s)
s = 'L\'orage gronde'
print(s)

a = 2
s = "valeur de a:"+str(a)
# f-string
s = f"valeur de {a=}"
print(s)

m = """Ligne01
Ligne02
Ligne03
"""
m = '''Ligne01
Ligne02
Ligne03
'''
print(m)
print(50*'-')
a=3
s ="a="*a
print(s)

print(50*'-')

word = 'Python'
print(word[2])
print(len(word))
print(word[len(word)-1])
print(word[-3])
# word[0] = "J"
# print(word)
word = "toto"
print(word)

a = 2
b = 2
print(hex(id(a)))
print(hex(id(b)))
# a=3
# print(hex(id(a)))
a = 4569876545698765
print(sys.getrefcount(4569876545698765))
b=4569876545698765
print(sys.getrefcount(4569876545698765))

print(50*'-')
word = 'Python'
print(word[2:5])# [2:4[
print(word[:5])# [2:4[
print(word[3:])# [2:4[
print(word[:])# [2:4[

