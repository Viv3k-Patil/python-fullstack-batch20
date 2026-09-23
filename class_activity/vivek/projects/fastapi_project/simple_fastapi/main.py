from fastapi import FastAPI


app = FastAPI()


@app.get("/hello")
def hello():
    return ["Parikshiti", "Suraj", "Yogita", "Vivek"]

@app.get("/health")
def hello():
    return {
        "health": "ok",
        "server running": "true"
    }



# localhost:8000/hello