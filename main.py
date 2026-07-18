from provinces import argentina_provinces
from localities import get_localitites
from pathlib import Path
import csv, json

def to_csv(output_dir, provinces):

    output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    for province in provinces:

        code = province["code"][-1]

        localities = get_localitites(code)

        fieldnames = localities[0].keys()

        filename = province["name"].replace(" ", "_").lower() + ".csv"

        filepath = output_dir / filename

        with open(filepath, "w", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=",")

            writer.writeheader()

            writer.writerows(localities)

def to_json(output_dir, provinces):

    output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    for province in provinces:

        code = province["code"][-1]

        data = {
            "iso_3166_2": province["code"],
            "provincia": province["name"],
            "localidades": get_localitites(code)
        }

        filename = province["name"].replace(" ", "_").lower() + ".json"

        filepath = output_dir / filename

        with open(filepath, "w", encoding="utf-8") as file:

            json.dump(data, file, indent=4, ensure_ascii=False)

# Generamos un directoro con todas las provincias e información de todas sus localidades en formato csv
to_csv("provincias_csv", argentina_provinces)

# Generamos un directoro con todas las provincias e información de todas sus localidades en formato json
to_json("provincias_json", argentina_provinces)
