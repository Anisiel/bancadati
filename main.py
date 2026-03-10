from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok", "message": "Backend attivo su Railway"}

@app.post("/etl/genera-crediti")
def genera_crediti():
    os.system("python etl/estrattore_crediti.py")
    return {"status": "ok", "message": "JSON crediti rigenerati"}
