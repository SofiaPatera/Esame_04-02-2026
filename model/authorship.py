from dataclasses import dataclass

@dataclass
class Authorship:
    object_id : int
    role : list
    artist_id: int

    def __str__(self):
        return self.object_id

    def __hash__(self):
        return hash(self.role)