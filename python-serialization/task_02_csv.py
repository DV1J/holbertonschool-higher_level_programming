#!/usr/bin/python3
"""reading data from one format (CSV) and converting
   it into another format (JSON) using serialization techniques.
"""

import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file to JSON."""
    try:
        with open(filename, 'r', encoding='utf-8') as filecsv:
            data = list(csv.DictReader(filecsv))

        with open('data.json', 'w', encoding='utf-8') as fj:
            json.dump(data, fj, indent=4)
            return True
    except Exception:
        return False
