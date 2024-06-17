#region importing the required libraries
import typing
from fastapi import FastAPI
import pydantic
from pizza_and_bread.models import TemperatureRecord, TemperatureResponse

import pandas as pd
#endregion


app  = FastAPI()

#this end point handles a get request. 
@app.get("/pizza/get_temperature", response_model=TemperatureRecord, tags=["pizza_temperature"])
async def print_text(text)-->pd.DataFrame:
    """
    docstring: Defining with async in case I have concurrent requests
    Returns: a dictionary with a message key and a value of "going to make pizza and bread"
    """
    text: str
    raw_data = TemperatureRecord

    
    #data = some transformation of TemperatureRecord
    
    try:
        #return the message
        return data
    except pydantic.ValidationError as e:
        #return the error message
        return {"error": str(e)}
    
