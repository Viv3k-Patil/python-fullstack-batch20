from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

class InsufficientBalanceError(Exception):
    def __init__(self, balance: float, requested: float):
        self.balance = balance
        self.requested = requested

@app.exception_handler(InsufficientBalanceError)
def insufficient_balance_handler(request: Request, exc: InsufficientBalanceError):
    return JSONResponse(
        status_code=400,
        content={
            "error": "InsufficientBalance",
            "message": f"You requested ₹{exc.requested} but only have ₹{exc.balance}",
        },
    )


@app.get("/withdraw/{amount}")
def withdraw(amount: float):
    balance = 1000
    if amount > balance:
        raise InsufficientBalanceError(balance=balance, requested=amount)
    return {"message": f"Withdrew ₹{amount}"}