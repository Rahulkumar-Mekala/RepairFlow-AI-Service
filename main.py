from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Mobile Repair AI Running"}

@app.get("/ai/test")
def test():
    return {"message": "Python connected successfully"}