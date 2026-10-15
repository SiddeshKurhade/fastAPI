from typing import Annotated, Dict, List , Optional

from pydantic import AnyUrl, BaseModel, EmailStr, Field


# here we add the all fields & here we define the type validation
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married : bool
    # or
    # married : bool = False                     #Here we define the default value suppose we dont pass the married field then it is set to be False 
    allergies: List[str]                         #Here we used typing List & Dict because in normal list we can not validate the type of list , But here we 
    contact_details: Dict[str,str]               #Here also we used Dict from the typing module Because we know this is Dictionary but using typing module also we define its key type & value type
    
    #Suppose we want to define one field as optional then we can define like below field
    #it means blood group is not mandatory
    #whenever we set optional then also reuired to add None like below example
    blood_group: Optional[str] = None

    #there are some built in validator 
    email: EmailStr                          #here 'EmailStr' email is validate | it gives an error when we upload wrong email formate data 
    linkedin_url: AnyUrl                     #here 'AnyUrl' is check uploaded url is correct or not , if url is uncorrect then it gives an error       

    #custom validation ;- it means we want the validation as per our use case 
    # suppose i want age is only between 0 to 120
    # Field method is used for  validation & also used for to add metadata
    age: int = Field(gt=0 , lt=120)        #gt -> greater than , lt = less than
    weight: float = Field(gt=0)            #weight is greater than 0 , suppose someone add there weight -78.9 then it gives an error
    name: str = Field(max_length=50)       #it means name character length is not exceed to 50 , if exceed then it gives an error

    #we also add metadata to fields using Field method & Annotated
    name: Annotated[str, Field(max_length=50,title='Name of patient',description='Give the name of the patient in less than 50 characters',examples=['Siddesh','John'])]
    married : Annotated[bool, Field(default=False,title='Set marrital status',examples=['True','False'])]  #in field method we also set the default value

    # in pydantic we pass int/float in the form of str the pydantic automatically convert it string into int/float
    weight: Annotated[float, Field(gt=0, strict=True)] # strict=True :- then using this we prevent for typecasting str-> int/float

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
    print(patient.blood_group)                #here return None because we dont pass the blood group
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