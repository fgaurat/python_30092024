import traceback

def divi(a,b):
    return a/b

def call_divi(a,b):
    try:
        print("open log")
        r = divi(a,b)
    finally:
        print("close log")
    return r

def main():

    try:
        a=2
        # b=int(input('b:'))
        b=0
        # c = a/b
        c = call_divi(a,b)
        print(c)
    except ZeroDivisionError as e:
        print("ZeroDivisionError",e)
    except TypeError as e:
        print("TypeError",e)
    except ValueError as e:
        print("ValueError",e)
    except Exception as e:
        print("Exception",e,type(e))

    # except:
    #     print("erreur !")
    #     traceback.print_exc()
    else:
        print("pas d'erreur")
    
    
    
    print("la suite du code")



if __name__=='__main__':
    main()
