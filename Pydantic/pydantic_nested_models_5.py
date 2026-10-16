from pydantic import BaseModel, EmailStr

class Address(BaseModel):
    city:str
    state:str
    pin_code:str

class Patient(BaseModel):
    name:str
    age:int
    email:EmailStr
    address:Address       #address khup chunks madhe store asto like city , state, pin code , etc


address_dict= {
    'city':'pune',
    'state':'maharashtra',
    'pin_code':'411028'
}
address1 = Address(**address_dict)

patient_dict={
    'name':'John',
    'age':23,
    'email':'john@gmail.com',
    'address':address1
}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin_code)