'''
Pydantic 

1) Define a pydantic model that represents the ideal schema of the data.
    - This includes the expected fields , their types & any validation constraints (eg. gt=0 for positive numbers )

2) Instantiate the model with raw input data(usually a dictionar or JSON - like structure)
    - Pydantic will automatically validate the data & coerce it into the correct python types (if possible).
    - if the data doesn't meet the models requirements, Pydantic raises a validationError

3) Pass the validated model object to functions or use it throughout  your codebase.
    - This ensures that every part of your program works with clean, type-safe & logically valid data
'''



from pydantic import BaseModel


# here we add the all fields & here we define the type validation
class Patient(BaseModel):
    name: str
    age: int



patient_info ={
    'name':'siddesh',
    'age':23
}

patient1 = Patient(**patient_info)

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('patient added successfully!')

insert_patient_data(patient1)


def update_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('update patient successfully!')

update_patient(patient1)