from fastapi import FastAPI, Depends

app = FastAPI()

@app.get('/health')
def check_health():
    return {
        "msg": "health is ok"
    }

def get_lucky_number_dependency():
    print('in get lucky number method')
    return 5


@app.get('/luck-number')
def get_luck_number(luck_number=Depends(get_lucky_number_dependency)):
    print('in get lucky number dependency method')
    return {
        "luck-number": luck_number
    }


def pagination_params(skip: int = 0, limit:int = 10):
    return {
            "skip": skip,
            "limit": limit
        }


@app.get('/users')
def get_users(pg_params=Depends(pagination_params)):
    return {
        "users": ["Parikshiti", "Suraj"],
        "pagination": pg_params
    }
    

@app.get('/products')
def get_products(pg_params=Depends(pagination_params)):
    return {
        "products": ["product1", "product2"],
        "pagination": pg_params
    }


class FakeDBSession:
    def __init__(self):
        print("🔌 DB session opened")

    def close(self):
        print("🔒 DB session closed")

    def get_user(self, user_id: int):
        return {"id": user_id, "name": "Priya"}

def get_db():
    db = FakeDBSession()
    try:
        yield db
    finally:
        db.close()

@app.get('/users/{user_id}')
def get_user_by_id(user_id:int, db:FakeDBSession = Depends(get_db)):
    user = db.get_user(user_id)
    return user