from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()


def get_current_user(authorization: str = Header(None)):
    if authorization != "Bearer secret-token-123":     # a STUB — a real app verifies a proper token
        raise HTTPException(status_code=401, detail="Not authenticated")
    return {"username": "priya", "role": "admin"}


@app.get("/profile")
def read_profile(current_user: dict = Depends(get_current_user)):
    return {"message": f"Welcome, {current_user['username']}!"}

class RoleChecker:
    def __init__(self, allowed_roles: list[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, current_user: dict = Depends(get_current_user)):
        if current_user["role"] not in self.allowed_roles:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return current_user


admin_only = RoleChecker(allowed_roles=["admin"])

@app.get("/admin-dashboard")
def admin_dashboard(user: dict = Depends(admin_only)):
    return {"message": f"Welcome to the admin dashboard, {user['username']}!"}