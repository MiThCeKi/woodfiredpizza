#region importing the required libraries
from typing import Optional, List
from fastapi import FastAPI
import pydantic
from pizza_and_bread.schemas.temperature import DTO_TemperatureResponse, DTO_TemperatureRecord
from pizza_and_bread.services.timestream_query_service import query_records_from_timestream
import logging
import boto3
impport watchtower
from .queries import queries

import pandas as pd
#endregion

#TODO put this in a function
# configure logging using logging and watchtower
boto3.setup_default_session(profile_name='pizzabread')
logger = logging.getLogger()
logger.setLevel(logging.ERROR)
cloudwatch_handler = watchtower.CloudWatchLogHandler(log_group='Timestream-errors', stream_name='pizza-bread-timestream')
logger.addHandler(cloudwatch_handler)


app  = FastAPI()

#this end point handles a get request.
@app.get("/pizza/get_temperature", response_model=DTO_TemperatureResponse | None)
async def get_temperature() -> DTO_TemperatureResponse | None:
    """
    docstring: Defining with async in case I have concurrent requests
    Returns: a DTO_TemperatureResponse object created from the records in the Timestream dict pulled by the query
    """
    try: 
        #use the query service to get a response
        query_response = query_records_from_timestream(queries.GET_RECENT_RECORDS.value)
        
        #from the response, create a record.
        records = [
            {
                "time": row['time'],
                "measure_name": row['measure_name'],
                "measure_value": row['measure_value::double'],
                "session_id": row['session_id']
            }
            for row in query_response
        ]
        
        #with pydantic I can just use the unpacking operator to create a DTO_TemperatureRecord object
        response_records = [DTO_TemperatureRecord(**record) for record in records]
             
        #again, with pydantic I can just use the unpacking operator to create a DTO_TemperatureResponse object
        return DTO_TemperatureResponse(records=response_records)
    
    except Exception as e:
        
        logger.error(f'Error querying the Timestream database. The error is {e}')
        raise HTTPException(status_code=500, detail=f"Error querying Timestream: {e}")

