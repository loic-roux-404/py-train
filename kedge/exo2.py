# from exo1 import read_file, write_to_file
import csv
from typing import List
from utils import read_file

def read_csv_keys(file: str, keys: List[str]) -> dict:
    reader = csv.DictReader(open(file, 'r', buffering=4096))

    d: dict[list[str]] = {}
    for key in keys:
        d[key] = []

    for row in reader:
        for key in keys:
            d[key].append(row.get(key))

    return d

def postals():
    metro_data = read_file("postalcode.txt")
    res = []
    for d in metro_data:
        _, postal = d.replace("\n", "").split(",")
        res.append(postal)

    print(res)

def descriptive_stats():
    metro_data = read_csv_keys(
        "Bordeaux-métropole.csv",
        ["surface_terrain", "valeur_fonciere"]
    )
    print(metro_data)

def main():
    postals()
    descriptive_stats()

main()
