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

# print(patient1)
# print(patient1.name)
# print(patient1.address.city)
# print(patient1.address.pin_code)



# model_dump() -> used to convert object to dictionary for exporting
# hita apan fields control karu shakto konte konte export karyche ahe te    
# temp = patient1.model_dump(include=['name']) #hita fakt name export hou shakta 
# temp = patient1.model_dump(exclude=['name'])  #hita name sodun baki sagle fields export hou shktat
# temp = patient1.model_dump(exclude_unset=True) #hita model banavtane ekhade field miss asal tr te exclude honr 
temp = patient1.model_dump()
print(temp)
print(type(temp))


#model_dump_json()-> used to convert object to json formate
temp_1 = patient1.model_dump_json()
print(temp_1)
print(type(temp_1))