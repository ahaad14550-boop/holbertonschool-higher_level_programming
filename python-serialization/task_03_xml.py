#!/usr/bin/env python3
"""
This module provides functions to serialize and deserialize XML data.
It converts Python dictionaries to XML format and parses them back.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file with a root element.
    Iterates through the dictionary items and writes the structure to disk.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Parses an XML file and converts its contents back into a Python dictionary.
    Iterates through all the child elements of the root to rebuild the data.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result_dict = {}

        for child in root:
            result_dict[child.tag] = child.text

        return result_dict
    except Exception:
        return {}
