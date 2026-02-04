from dataclasses import dataclass
@dataclass
class Artist:
    artist_id : int
    name : str

    def __str__(self):
        return self.name





