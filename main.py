import json

from fastapi import FastAPI, HTTPException, Path, Query 

#HTTPException-> this is the special built in exception in fastAPI used to return custom HTTP error response when something goes wrong in your API
#instead of returning a normal JSON or crashing the server , you can gracefully raise an error with:
# a proper HTTP status code (like 404,400,403, etc)
# a custom error message
# optional extra headers


#Path() -> this function in fastapi is used to provide metadata, validation rules,
# and documentation hints for path parameters in your API endpoints

app =  FastAPI()

#To load the data from the file i.e patients.json
def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)

    return data;

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
def view_patient(p_id:int = Path(..., description='Id of the patient in the DB', example='1')):
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