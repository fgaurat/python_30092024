# import fibo as fb
# fb.fib(100)
import sys
# sys.path.append('/ufs/guido/lib/python')
# from fibo import fib as f
from fibo import fib

# def fib(a):
#     print("fib",a)

def main(v):
    fib(v)

if __name__=='__main__':
    print("argv",sys.argv)
    v = int(sys.argv[-1])
    main(v)


