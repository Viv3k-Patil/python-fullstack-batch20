from fastapi import FastAPI
import asyncpg

app = FastAPI()

@app.get("/employees")
async def root():

    connection = await asyncpg.connect(
        user="postgres",
        password="password",
        database="demodb",
        host="localhost",
        port=5432
    )

    result = await connection.fetch(
        "SELECT * FROM employees"
    )

    await connection.close()

    return {
        "employees":result,
        "success": "true"
    }