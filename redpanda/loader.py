import json
from pathlib import Path

BASE = Path(__file__).parent / "data"


def load_json(name: str) -> dict:
    with open(BASE / f"{name}.json", "r", encoding="utf-8") as f:
        return json.load(f)


KEYWORDS = load_json("keywords")
BUILTINS = load_json("builtins")
CONSTANTS = load_json("constants")