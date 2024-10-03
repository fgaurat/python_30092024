
def log(func):


    def wrapper(*args,**kwargs):
        print("LOG BEFORE",args,kwargs,func)
        r = func(*args,**kwargs)
        print("LOG AFTER",r)
        return r 
    
    return wrapper

@log
def say_hello(name,firstName):

    r=f"Hello {name} {firstName}"

    return r

def main():
    r = say_hello("GAURAT","fred")
    print(r)

if __name__=='__main__':
    main()
