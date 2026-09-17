import hashlib

from class_activity.vivek.projects.phase7_full_project.models.user import User
from class_activity.vivek.projects.phase7_full_project.exceptions import UserAlreadyExistsError, AuthenticationError


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()  # never store raw passwords!


class AuthService:
    def __init__(self):
        self.users = {}  # phone -> User

    def register(self, name, phone, email, password):
        if phone in self.users:
            raise UserAlreadyExistsError("User already registered with this phone number")
        user = User(name, phone, email, hash_password(password))
        self.users[phone] = user
        return user

    def login(self, phone, password):
        user = self.users.get(phone)
        if user is None or not user.check_password(hash_password(password)):
            raise AuthenticationError("Invalid phone number or password")
        return user

    def load_users(self, users_dict):
        """Rehydrate users from persisted data on startup."""
        self.users = {phone: User.from_dict(data) for phone, data in users_dict.items()}

    def dump_users(self):
        """Serialize users for persistence."""
        return {phone: user.to_dict() for phone, user in self.users.items()}
