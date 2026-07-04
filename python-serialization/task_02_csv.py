#!/usr/bin/env python3
"""
This module provides a function to convert CSV data into JSON format.
It reads from a source CSV file and writes the structured data to data.json.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts the contents of a CSV file into a JSON file named data.json.
    Returns True if the conversion succeeds, and False if an error occurs.
    """
    try:
        data_list = []
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data_list.append(row)

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file)

        return True
    except Exception:
        return False
