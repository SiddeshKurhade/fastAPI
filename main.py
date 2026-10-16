import json

from fastapi import FastAPI, HTTPException, Path, Query 
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal,Optional
from fastapi.responses import JSONResponse

#HTTPException-> this is the special built in exception in fastAPI used to return custom HTTP error response when something goes wrong in your API
#instead of returning a normal JSON or crashing the server , you can gracefully raise an error with:
# a proper HTTP status code (like 404,400,403, etc)
# a custom error message
# optional extra headers


#Path() -> this function in fastapi is used to provide metadata, validation rules,
# and documentation hints for path parameters in your API endpoints

app =  FastAPI()

class Patient(BaseModel):
    patient_id: Annotated[int,Field(...,description="Enter the patient Id")]
    name: Annotated[str,Field(...,description="Enter the patient Name")]
    city: Annotated[str,Field(...,description="City where the patient is living")]
    age:Annotated[int,Field(...,gt=0,lt=120,description="Current Age of the patient")]
    gender:Annotated[Literal['male','femal','other'],Field(...,description="Enter the gender of the patient")]
    height:Annotated[float,Field(...,gt=0,description="Height of the patient in meters")]
    weight:Annotated[float,Field(...,gt=0,description="Weight of the patient in kg")]


    @computed_field
    @property
    def bmi(self)->float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

class UpdatePatient(BaseModel):
    #here we remove '...' this because we dont want any field mandetory 
    name: Annotated[Optional[str],Field(None,description="Enter the patient Name")]
    city: Annotated[Optional[str],Field(None,description="City where the patient is living")]
    age:Annotated[Optional[int],Field(None,gt=0,lt=120,description="Current Age of the patient")]
    gender:Annotated[Optional[Literal['male','femal','other']],Field(None,description="Enter the gender of the patient")]
    height:Annotated[Optional[float],Field(None,gt=0,description="Height of the patient in meters")]
    weight:Annotated[Optional[float],Field(None,gt=0,description="Weight of the patient in kg")]

    
#To load the data from the file i.e patients.json
def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data;

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)

@app.get("/")
def hello():
    return {'message':'Patient Management Systems'}

@app.get("/about")
def about():
    return {'message':'A fully functional API to manage patients records'}


#To fetch all data from the patient file 
@app.get("/view")
def view():
    data = load_data()
    return data;


#Fetch specific patient data on basis of id
@app.get('/patient/{p_id}')
def view_patient(p_id:int = Path(..., description='Id of the patient in the DB', examples='1')):
    #load all data 
    data = load_data()

    # Search for the patient by ID
    for patient in data:
        if patient["patient_id"] == p_id:
            return patient

    raise HTTPException(
        status_code=404,
        detail="Patient Id Not Found!"
    )


#Query Parameter
#Query parameters are optional key-value pairs appended to the end of a URL, used to pass additional data to the server in an HTTP request.
#They are typically employed for operations like filtering , sorting, searching & pagination,  without altering the endpoint path itself
# ex;- /patients?city=Pune&sort_by=age 

#The ? marks the start of query parameters.
#Each parameter is a key-value pair
#Multiple parameters are separated by & 

#Query() is a utility  function provided by FastAPI to declare , validate & document query parameters in your API endpoints
# It allows you to :
#    Set default values
#    Enforce validation rules
#    Add metadata like description, title, examples
 

# Query(...,description='Sort on the basis of age')   in first parameter i write ... it means parameter is required 
# Query('asc',description='sort in asc or desc order')  here parameter is not mandatory

@app.get('/sort')
def sort_patients(sort_by:str = Query(...,description='Sort on the basis of age'), order:str=Query('asc',description='sort in asc or desc order')):
    valid_fields = ['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'Invalid fields select from {valid_fields}')

    if order not in ['asc','desc']:
         raise HTTPException(status_code=400,detail='Invalid order select between asc & desc')

    data = load_data()
    sort_order = True if order=='desc' else False    #here we set the flag for asc & desc 
    sorted_data = sorted(data, key = lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorted_data;




@app.post('/create')
def create_patient(patient:Patient):

    #Load patient data
    data = load_data()

    #check if patient allready created

    for p in data:
        if p["patient_id"] == patient.patient_id:
            raise HTTPException(status_code=400,detail='Patient Allready Created !')

    #new patient add to database
    new_patient = patient.model_dump()
    data.append(new_patient)

    #save data in patients.json file
    save_data(data)

    return JSONResponse(
        status_code=201,
        content={'message':'Record Created successfully!'}
    )



@app.put('/edit/{p_id}')
def update_patient(p_id:int,patient_update:UpdatePatient):

    #Load patient data
    data = load_data()

    # Find the existing patient
    for p in data:
        if p["patient_id"] == p_id:

            # Update existing patient information
            existing_patient_info = p

            # Convert update model to dictionary
            update_data = patient_update.model_dump(exclude_unset=True)

            # Update only the provided fields
            for key, value in update_data.items():
                existing_patient_info[key] = value


            #suppose we update the weight or height so according to this we can update our bmi  
            #Now convert latest updated value into object for updated bmi 
            existing_patient_info['patient_id']=p_id
            updated_patient_object = Patient(**existing_patient_info)   #here we convert dictionary to object 

            #pydantic object -> dictionary
            existing_patient_info = updated_patient_object.model_dump(exclude='patient_id')

            # Update the original patient record with recalculated BMI
            p.update(existing_patient_info)

            # Save updated data to JSON file
            save_data(data)

            return JSONResponse(
                status_code=200,
                content={
                            "message": "Patient updated successfully!",
                            "patient": existing_patient_info
                        }
            )
        
    # If patient is not found
    raise HTTPException(
        status_code=404,
        detail="Patient Not Found!"
    )



@app.delete('/delete/{p_id}')
def delete_patient(p_id:int):
    #Load patient data
    data = load_data()

    #check if patient allready existed or nnot
    for p in data:
        if p["patient_id"] == p_id:
            # Remove patient from the list
            data.remove(p)
            # Save updated data to JSON file
            save_data(data)
            return JSONResponse(
                status_code=200,
                content={
                            'message':'Patient data deleted successfully!',
                        }
            )



    raise HTTPException(status_code=400,detail=f'Patient with this {p_id} is not present!')
