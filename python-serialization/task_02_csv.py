#!/usr/bin/python3
"""reading data from one format (CSV) and converting
   it into another format (JSON) using serialization techniques.
"""

import csv
import json


def convert_csv_to_json(filename):
    with open(filename, 'r') as filecsv:
        data = list(csv.DictReader(filecsv))
    with open(filename, 'w') as fj:
        json.dump(data, fj)
