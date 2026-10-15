
# case 1:
# def insert_patient_data(name,age):

#     print(name)
#     print(age)
#     print("inserted into database")

# insert_patient_data('siddesh','kurhade')  # when we call function here we see any datatype so we can give any type of data while calling



# case 2:
# def insert_patient_data_with_datatype(name:str,age:int):

#     print(name)
#     print(age)
#     print("inserted into database")

# insert_patient_data_with_datatype('siddesh','23')  
# here we can see the datatype of the variable
# But in case we dont see that type & we write anything then here we can not get an error as it is value is store in the database 
# it means here only inform us to write in a proper formate , here dont validate the datatype



# case 3:
# def insert_patient_data_with_validation(name:str,age:int):

#     if type(name)==str and type(age)==int:
#         print(name)
#         print(age)
#         print('inserted into database')

#     else:
#         raise TypeError('Incorrect data type')

# # insert_patient_data_with_validation('sidd','23')   #here we gives an typeerror because we pass age as a string
# insert_patient_data_with_validation('sidd',23)       # here we dont get an error because we pass age as a int 

#but this is not a scalable way to write this code

# suppose we want to update this data then inside that function  also written validation code 
# we re-write the code again and again

# this above all cases are for why we use pydantic for validation 


