

# employee database
# authentication - who are you?

employees = {
    "vaibhav": {
        "password": "vaibhav123",
        "role": "admin"
    },
    "yogita": {
            "password": "yogita123",
            "role": "manager"
    },
    "parikshiti": {
            "password": "parikshiti123",
            "role": "employee"
    }
}

# permission information
# authorization what are you allowed to do?

permissions = {
    "view_reports": ["admin", "manager", "employee"],
    "approve_leave": ["admin", "manager"],
    "delete_employee": ["admin"]
}


# current logged in user

current_user = "None"


# access control decorator

def requires_permission(action):
    def decorator(func: function):
        def wrapper(*args, **kwargs):
            # check if there is user who logged in
            if current_user is None:
                print("❌ Access Denied: No user is logged in.")

            # get user role
            user_role = employees[current_user]["role"]

            # if that role has permission to do mentioned things
            if user_role not in permissions.get(action, []):
                print(f"❌ Access Denied: '{current_user}' ({user_role}) cannot perform '{action}'.")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator


# authentication

def login(username:str, password: str):
    global current_user

    if username not in employees:
        print("username not availabel")
        return False

    if employees[username]["password"] != password:
        print("password chukicha aahe")

    current_user = username
    return True
    

def logout():
    global current_user
    current_user = None
    print("logout")

# business logic

@requires_permission("view_reports")
def view_reports():
    print("view reports")

@requires_permission("approve_leave")
def approve_leave():
    print("approve leave")

@requires_permission("delete_employee")
def delete_employee():
    print("delete employee")


# authentication, WHO ARE YOU?
login("parikshiti","parikshiti123")
view_reports()
approve_leave()
delete_employee()
logout()

login("vaibhav", "vaibhav123")
view_reports()
approve_leave()
delete_employee()
logout()