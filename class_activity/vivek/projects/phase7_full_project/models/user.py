class User:
    """Represents a registered bank customer."""

    def __init__(self, name, phone, email, password_hash):
        self.name = name
        self.phone = phone
        self.email = email
        self._password_hash = password_hash  # encapsulated - never store raw passwords!

    def check_password(self, password_hash):
        return self._password_hash == password_hash

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "password_hash": self._password_hash,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["phone"], data["email"], data["password_hash"])
