from typing import Annotated, Dict, List , Optional

from pydantic import AnyUrl, BaseModel, EmailStr,  computed_field


# here we add the all fields & here we define the type validation
class Patient(BaseModel):
    name: str
    age: int
    email:EmailStr
    weight: float   #in kg
    height: float   #in meters
    married : bool
    allergies: List[str]                        
    contact_details: Dict[str,str]               


    #computeed fields:- hita apan on the go madhe new field pahije asal varchy field varun te apan calculate caru shakto
    # suppose apan user kadun bmi ghet nahi but apan weight & height varun calculate karu shakto using computed fields

    @computed_field
    @property
    def calculate_bmi(self)-> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

patient_info ={
    'name':'siddesh',
    'age':70,
    'email':'sid@hdfc.com',
    'weight':67.45,
    'married':False,
    "height": 1.75,
    "weight": 72,
    'allergies':['pollen','dust'],
    'contact_details':{
        'emergency':'567893987',
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
    print('patient added successfully!')

insert_patient_data(patient1)


def update_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.allergies[0])
    print(patient.married)
    print(patient.contact_details)
    print(patient.calculate_bmi)
    print('update patient successfully!')

update_patient(patient1)