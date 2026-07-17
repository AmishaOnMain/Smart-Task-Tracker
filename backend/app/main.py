from fastapi import FastAPI

app= FastAPI(

  title= "AI Productivity Dashboard API",

  description= "Backend API for the AI Productivity Dashboard",

  version= "1.0.0",
)

@app.get("/")

def root():

  return{

    "message": "Welcome to the AI Productivity Dashboard API"
  }