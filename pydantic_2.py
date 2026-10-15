from typing import Dict, List

from pydantic import BaseModel


# here we add the all fields & here we define the type validation
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married : bool
    allergies: List[str]                         #Here we used typing List & Dict because in normal list we can not validate the type of list , But here we 
    contact_details: Dict[str,str]



patient_info ={
    'name':'siddesh',
    'age':23,
    'weight':67.45,
    'married':False,
    'allergies':['pollen','dust'],
    'contact_details':{
        'email':'sid@gmail.com',
        'phone_no':'7879037456'
    }
}

patient1 = Patient(**patient_info)

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.allergies[0])
    print(patient.married)
    print(patient.contact_details)
    print(patient.contact_details['email'])
    print('patient added successfully!')

insert_patient_data(patient1)


def update_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.allergies[0])
    print(patient.married)
    print(patient.contact_details)
    print(patient.contact_details['email'])
    print('update patient successfully!')

update_patient(patient1)