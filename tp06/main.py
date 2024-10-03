from Rectangle import Rectangle
from Carre import Carre
from Cercle import Cercle

def main01():
    the_r = Rectangle(2,5)
    l = the_r.get_longueur()
    print(l)# 2
    print(the_r.get_largeur())# 5
    
    the_r.set_longueur(12)
    print(the_r.get_longueur())# 12

    # the_r.set_largeur(-12)
    # print(the_r.get_largeur())# -12
    print(the_r.get_surface())
    
    str_the_r = str(the_r)
    print(str_the_r)
    print(50*'-')
    the_r = Rectangle(2,5)
    the_r1 = Rectangle(2,5)
    # if the_r.__eq__(the_r1)
    if the_r == the_r1:
        print("Youhou")
    else:
        print("Pas Youhou")

def main02():
    the_r = Rectangle(2,5)
    print(the_r.longueur)
    the_r.longueur=12
    print(the_r.longueur)

def main03():
    c = Carre(2)
    print("cote",c.cote)
    print("surface",c.get_surface())
    c.cote = 4
    print("cote",c.cote)
    print("surface",c.get_surface())
    c.longueur

def main():
    ce = Cercle(2)
    s = ce.get_surface()
    print("surface",s)

if __name__=='__main__':
    main()
