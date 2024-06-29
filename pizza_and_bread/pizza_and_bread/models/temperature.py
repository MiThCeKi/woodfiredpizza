# pylint: disable=missing-docstring,invalid-name

from sqlalchemy import Column, Integer, Float, String, DateTime
from pizza_and_bread.models.base import Base



class DB_TemperatureRecord(Base):
    __tablename__ = "temperature_records"
    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float, index=True)
    time = Column(DateTime, index=True)
    oven_id = Column(String, default="1")
    
    
