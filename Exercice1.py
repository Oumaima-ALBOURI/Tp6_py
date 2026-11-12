
from dataclasses import dataclass, asdict
import json


@dataclass(frozen=True, slots=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)


# Programme principal
livre = Livre("1984", "George Orwell", 1949, 9.90)

print(livre.to_json())
