import json
from pathlib import Path

DATA_FILE = Path("library_data.json")

def save_books(books):
    with open(DATA_FILE, "w") as file:
        json.dump(books, file, indent=4)

def load_books():
      if not DATA_FILE.exists():
          return None

      try:
           with open(DATA_FILE, "r") as file:
                return json.load(file)
      except (json.JSONDecodeError, OSError):
           return None