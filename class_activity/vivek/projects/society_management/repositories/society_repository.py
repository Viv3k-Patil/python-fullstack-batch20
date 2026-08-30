"""
society_repository.py

Repository pattern: gives the rest of the app a simple save/get interface,
hiding HOW societies are actually stored. Right now it's just an in-memory
dict, but this is the seam where you'd later swap in a real database
without touching any service or model code.
"""

from models.society import Society


class SocietyRepository:
    def __init__(self):
        self._societies: dict[str, Society] = {}

    def add(self, society: Society):
        self._societies[society.name] = society

    def get(self, name: str) -> Society:
        return self._societies[name]

    def exists(self, name: str) -> bool:
        return name in self._societies

    def list_all(self) -> list[Society]:
        return list(self._societies.values())
