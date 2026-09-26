from fastapi import FastAPI, Depends

app = FastAPI()

def get_query_param(q: str = "default_value"):
    return q

@app.get("/items/")
def read_items(q: str = Depends(get_query_param)):
    return {"q": q}