#region importing the required libraries
import typing
from fastapi import FastAPI
import pydantic
from pizza_and_bread.models import TemperatureRecord, TemperatureResponse

import pandas as pd
#endregion


app  = FastAPI()

#this end point handles a get request. 
@app.get("/pizza/get_temperature", response_model=DTO_TemperatureRecord, tags=["pizza_temperature"])
async def print_text(text)--> DTO_TemperatureRecord:
    """
    docstring: Defining with async in case I have concurrent requests
    Returns: a dictionary 
    """


    #data = some transformation of DTO_TemperatureRecord
    
    try:
        #return the message
        return data
    except pydantic.ValidationError as e:
        #return the error message
        return {"Error while getting the data": str(e)}
    
