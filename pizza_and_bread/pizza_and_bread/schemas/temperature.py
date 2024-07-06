# pylint: disable=missing-docstring,invalid-name

#region imports
from typing import List
from pydantic import BaseModel

#type aliasing
""" String of format `abc_<7 digit number>"""
Id = type(str)

#session is an object that might have a property that is the date but also a property such as 1, 2, 3 etc
#endregion


class DTO_TemperatureRecord(BaseModel):
    #Docstring: this is a serializable model that FastAPI expects to work with. 
    measure_value: float
    time: str
    session_id: str
    measure_name: str

class DTO_TemperatureResponse(BaseModel):
    records: List[DTO_TemperatureRecord]
    
    
    
