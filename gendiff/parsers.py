import json
from pathlib import Path

import yaml


def parse_file(file_path):
    extension = Path(file_path).suffix.lower()

    with open(file_path, encoding="utf-8") as file:
        if extension == ".json":
            return json.load(file)
        if extension in (".yml", ".yaml"):
            return yaml.safe_load(file)

    raise ValueError(f"Unsupported file format: {extension}")
