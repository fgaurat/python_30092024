from dataclasses import dataclass

@dataclass
class Employee:
    id:int=0
    first_name:str=""
    last_name:str=""
    email:str=""
    gender:str=""
    ip_address:str=""