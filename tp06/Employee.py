from dataclasses import dataclass

@dataclass
class Employee:
    id:int=0
    last_name:str=""
    first_name:str=""
    age:int=0


    def toto(self):
        print("truc")


def main():
    e = Employee(1,"DURNAD","Robnert",87)
    print(e)

if __name__=='__main__':
    main()
