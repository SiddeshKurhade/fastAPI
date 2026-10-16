from typing import Annotated, Dict, List , Optional

from pydantic import AnyUrl, BaseModel, EmailStr, Field , field_validator


# here we add the all fields & here we define the type validation
class Patient(BaseModel):
    name: str
    age: int
    email:EmailStr
    weight: float
    married : bool
    allergies: List[str]                        
    contact_details: Dict[str,str]               

    #using field valdator we can perform custom validation on the field
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):                       #here cls-> used for any other method present inside the class that method also access inside this class & value is for email field value
        valid_domain=['hdfc.com','icici.com']

        #abc@gmail.com
        domain_name = value.split('@')[-1]       #here we get 'gmail.com'

        if domain_name not in valid_domain:
            raise ValueError('Not a valid domain')

        return value

    @field_validator('name')
    @classmethod
    def name_validation(cls,value):
        return value.upper();


    #here we set mode='before' & mode='after'
    #before means-> type conversion chy adhi 
    #after means-> type conversion chy nantr

    #suppose we are add age:'23' as a string and we applied validation before conversion then it gives an error because pydantic not compare string & integer
    # then we set mode='after' -> here firstly type is converted then validation is applied
    @field_validator('age', mode='before')
    @classmethod
    def age_validation(cls,value):
        if 0 < value <100:
            return value
        else:
            raise ValueError('Age should be between 0 and 100')

    #in field validator we can not validate 2 or more fields simultaneously 
    #for ex:- I want to add validation on : jynch age 60 peksha jast ahe tynchy contact_details madhe emergancy_no mandetory ahe
    #this validation is not possible throught the field validator

    #model_validator is used for above problem

patient_info ={
    'name':'siddesh',
    'age':23,
    'email':'sid@hdfc.com',
    'weight':67.45,
    'married':False,
    'allergies':['pollen','dust'],
    'contact_details':{
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