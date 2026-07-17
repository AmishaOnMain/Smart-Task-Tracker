from fastapi import FastAPI

from app.database.init_db import init_db

app= FastAPI(

  title= "AI Productivity Dashboard API",

  version= "1.0.0",
)


#@app.on_event("startup")
#def startup():
  #init_db()

@app.get("/")

def root():

  return{

    "message": "API is running"
  }