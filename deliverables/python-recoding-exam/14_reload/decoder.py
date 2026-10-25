"""Provided dependency. Do not edit. Not part of the candidate's assessed work."""
import json

def _unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate object member")
        result[key] = value
    return result

def decode_catalog(text):
    if not isinstance(text, str):
        raise TypeError("Expected JSON text")
    data = json.loads(text, object_pairs_hook=_unique_pairs)
    if not isinstance(data, list):
        raise ValueError("Expected list")
    seen = set()
    for record in data:
        if not isinstance(record, dict) or not {"id", "name", "quantity"} <= record.keys():
            raise ValueError("Invalid record")
        for key in ("id", "name"):
            value = record[key]
            if not isinstance(value, str) or not value or value != value.strip():
                raise ValueError("Invalid label")
        if type(record["quantity"]) is not int or record["quantity"] < 0:
            raise ValueError("Invalid quantity")
        if record["id"] in seen:
            raise ValueError("Duplicate ID")
        seen.add(record["id"])
    return data
