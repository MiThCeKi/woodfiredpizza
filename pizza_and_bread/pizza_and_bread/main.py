


#region importing the required libraries
from fastapi import FastAPI
#endregion


app  = FastAPI()

#this end point handles a get request. 
@app.get("/")
async def print_text(): #defining with async in case I have concurrent requests
    return {"message": "going to make pizza and bread"}

