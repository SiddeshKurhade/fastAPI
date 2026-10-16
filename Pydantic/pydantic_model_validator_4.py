from typing import Annotated, Dict, List , Optional

from pydantic import AnyUrl, BaseModel, EmailStr,  model_validator


# here we add the all fields & here we define the type validation
class Patient(BaseModel):
    name: str
    age: int
    email:EmailStr
    weight: float
    married : bool
    allergies: List[str]                        
    contact_details: Dict[str,str]               


    #we can use all model fields here , so we can validate 2 or more fields inside this model_validator
    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age >= 60 and 'emergency' not in self.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')

        return self

patient_info ={
    'name':'siddesh',
    'age':70,
    'email':'sid@hdfc.com',
    'weight':67.45,
    'married':False,
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
    print('update patient successfully!')

update_patient(patient1)