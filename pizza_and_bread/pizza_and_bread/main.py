#region importing the required libraries
from typing import Optional, List
from fastapi import FastAPI
import pydantic
from pizza_and_bread.schemas.temperature import DTO_TemperatureResponse, DTO_TemperatureRecord
from pizza_and_bread.services.timestream_query_service import query_records_from_timestream
import logging
import boto3
from pizza_and_bread.logging.logging import set_up_logging
import watchtower
from pizza_and_bread.services.queries import Queries
from fastapi import HTTPException

import pandas as pd
#endregion

boto3.setup_default_session(profile_name='pizzabread')

# configure logging using logging and watchtower
logger = set_up_logging(log_group='Timestream-query-errors', stream_name='pizza-bread-timestream')

app  = FastAPI()

#this end point handles a get request.
@app.get("/pizza/get_temperature", response_model=DTO_TemperatureResponse)
async def get_temperature() -> DTO_TemperatureResponse:
    """
    docstring: Defining with async in case I have concurrent requests
    Returns: a DTO_TemperatureResponse object created from the records in the Timestream dict pulled by the query
    """
    try: 
        #use the query service to get a response
        query_response = query_records_from_timestream(Queries.GET_RECENT_RECORDS.value)
        
        #from the response, create a record.
        records = [
            {
                "time": row['Data'][0]['ScalarValue'],
                "measure_name": row['Data'][1]['ScalarValue'],
                "measure_value": row['Data'][2]['ScalarValue'],
                "session_id": row['Data'][3]['ScalarValue']
            }
            for row in query_response['Rows']
        ]
    
        #with pydantic I can just use the unpacking operator to create a DTO_TemperatureRecord object
        response_records = [DTO_TemperatureRecord(**record) for record in records]
             
        #again, with pydantic I can just use the unpacking operator to create a DTO_TemperatureResponse object
        return DTO_TemperatureResponse(records=response_records)
    
    except Exception as e:
        #print as well as log the errors.
        logger.error(f'Error querying the Timestream database. The error is {e}')
        raise HTTPException(status_code=500, detail=f"Error querying Timestream: {e}")

