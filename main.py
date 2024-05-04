from fastapi import FastAPI
from config.database import Base 

app = FastAPI()
app.title = "hotel"

@app.app.get('/api/hotel')
def hotel():
    
    return